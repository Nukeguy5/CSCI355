
from diskpy import Disk
import numpy as np
import blocks
from blockbitmap import BlockBitMap
import time

def fs_format(disk_name):
    print("\tFormatting...")

    # Read Super Block into buffer
    mydisk = Disk.disk_open(disk_name)
    sblock = Disk.disk_read(mydisk, 0)

    # Super Block Info
    nblocks = Disk.disk_size(mydisk)//Disk.BLOCK_SIZE
    ninode_blocks = nblocks//10  # Make 10% of blocks to be inode_blocks
    ninodes = Disk.BLOCK_SIZE//blocks.Inode.size * ninode_blocks
    dentry = 0
    dataBitmap_block = 1
    inodeBitmap_block = 2
    dataBlock_start = 3 + ninode_blocks
    inodeBlock_start = 3

    # Create buffer to write new data to disk
    blank_blocks = np.zeros(shape=(nblocks, Disk.BLOCK_SIZE), dtype='int8')
    sblock = blocks.Superblock.make_block(nblocks, ninode_blocks, ninodes, dentry, dataBitmap_block, inodeBitmap_block, dataBlock_start, inodeBlock_start)
    iblock = blocks.InodeBlock.make_block()
    
    # Initialize bitmaps
    data_bitmap = BlockBitMap(Disk.BLOCK_SIZE, dataBitmap_block)
    inode_bitmap = BlockBitMap(Disk.BLOCK_SIZE, inodeBitmap_block)
    ndata_blocks = nblocks - ninode_blocks - 3  # don't count super block or bitmaps
    data_bitmap.init(ndata_blocks)
    inode_bitmap.init(ninodes)
    inode_bitmap.setUsed(0)  # set inode 0 to USED

    # Write initial blocks to array
    blank_blocks[0] = sblock
    blank_blocks[1] = data_bitmap.saveToDisk()
    blank_blocks[2] = inode_bitmap.saveToDisk()

    for i in range(ninode_blocks):
        i += 3  # don't overwrite superblock or bitmaps
        blank_blocks[i] = iblock
    
    Disk.disk_write(mydisk, 0, blank_blocks)
    time.sleep(.25)
    # Create the File System
    fs_create(mydisk)

    print("\tFormat Complete.")

def fs_debug():
    pass

def fs_mount():
    pass

def fs_create(open_file):
    # Inode 0 is used as Error data inode
    # Inode 1 is root directory

    sblock = Disk.disk_read(open_file, 0)
    dentry = sblock[4]

    # Add Inode Bitmap to buffer
    inodeNum = 1
    inode_bitmap = BlockBitMap(Disk.BLOCK_SIZE, 2)
    inode_bitmap.blockBitMap = Disk.disk_read(open_file, inode_bitmap.blockNumber)
    
    # Add Data Bitmap to buffer
    data_bitmap = BlockBitMap(Disk.BLOCK_SIZE, 1)
    data_bitmap.blockBitMap = Disk.disk_read(open_file, 1)
    data_bitmap.setUsed(0)  # Mark data block as used
    
    fs_dict = {'.':1, '..':1, 'etc':2, 'bin':3}

    for directory in fs_dict:
        inodeNum = fs_dict[directory]
        change_inode(open_file, inodeNum, dentry)
        inode_bitmap.setUsed(inodeNum)  # Mark inode as used

    Disk.disk_write(open_file, 1, data_bitmap.saveToDisk())
    Disk.disk_write(open_file, inode_bitmap.blockNumber, inode_bitmap.saveToDisk())

    # Find datablock
    data_blockStart = sblock[7]
    real_dblockNum = data_blockStart + dentry
    data_block = Disk.disk_read(open_file, real_dblockNum)

    # Change data block
    ptr_div = Disk.BLOCK_SIZE//32  # to use to divide the data block 
    
    for i in range(len(fs_dict)):
        fs_lst = [item for item in fs_dict]
        data_block[ptr_div*i] = fs_dict[fs_lst[i]]
        str_conv = [int.from_bytes(bytes(char, Disk.ENCODING), Disk.BYTEORDER) for char in fs_lst[i]]
        # data_block[ptr_div*i+1] = str_conv

        for j in range(len(str_conv)):
            data_block[ptr_div*i+(j+1)] = str_conv[j]

    Disk.disk_write(open_file, real_dblockNum, bytearray(data_block))

def fs_delete(file):
    pass

def fs_getsize(file):
    pass

def fs_read(file, length, offset):
    pass

def fs_write(file, data, length, offset):   
    # To get to inode 
        # logical block num => inodeNum//16 
        # superblock[8] = inodeBlockStart
        # real block num => logical + inodeBlockStart
        # inode offeset => inodeNum % 16 * blocks.Inode.size
    pass

def fs_findfree(open_file, blocknum):
    bitmap = BlockBitMap(Disk.BLOCK_SIZE, blocknum)
    disk_read = Disk.disk_read(open_file, blocknum)
    bitmap.blockBitMap = disk_read
    free_space = bitmap.findFree()
    
    return free_space

def change_inode(open_file, inodeNum, dblockNum, directory=True):
    # Find Inode
    inode_size = blocks.Inode.size
    sblock = Disk.disk_read(open_file, 0)
    inode_blockStart = sblock[8]
    ninodes_in_block = Disk.BLOCK_SIZE//inode_size
    inode_blockNum = inodeNum//ninodes_in_block
    real_blockNum = inode_blockNum + inode_blockStart
    inode_block = Disk.disk_read(open_file, real_blockNum)

    # Make changes to Inode
    inode_size = blocks.Inode.size
    buffer = np.zeros(shape=(Disk.BLOCK_SIZE), dtype='int8')
    if directory:
        inode_block[inodeNum*inode_size+0] = blocks.Inode.DIR
    else:
        inode_block[inodeNum*inode_size+0] = blocks.Inode.FILE
    inode_block[inodeNum*inode_size+1] = inode_size
    inode_block[inodeNum*inode_size+2] = dblockNum
    for i in range(len(inode_block)):
        buffer[i] = inode_block[i]
    Disk.disk_write(open_file, real_blockNum, buffer)

# Have to read the whole file and rewrite it to disk because of how python works
# def add_disk_to_buffer(open_file):
#     sblock = Disk.disk_read(open_file, 0)  #read superblock to determine number of blocks on disk
#     nblocks = sblock[1]
#     disk_blocks = np.zeros(shape=(nblocks, Disk.BLOCK_SIZE//4), dtype=Disk.CELLSIZE)

#     for i in range(nblocks):
#         disk_read = Disk.disk_read(open_file, i)
#         disk_blocks[i] = disk_read
    
#     return disk_blocks
