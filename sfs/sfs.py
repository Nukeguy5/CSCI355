
from diskpy import Disk
import numpy as np
import blocks
from blockbitmap import BlockBitMap

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

    print("\tFormat Complete.")

def fs_debug():
    pass

def fs_mount():
    pass

def fs_create(open_file):
    # Inode 0 is used as Error data inode
    # Inode 1 is root directory

    disk_blocks = add_disk_to_buffer(open_file)

    sblock = disk_blocks[0]
    dentry = sblock[4]

    # Add Inode Bitmap to buffer
    inodeNum = 1
    inode_bitmap = BlockBitMap(Disk.BLOCK_SIZE, 2)
    inode_bitmap.blockBitMap = disk_blocks[2]
    inode_bitmap.setUsed(inodeNum)  # Mark inode as used
    disk_blocks[2] = inode_bitmap.saveToDisk()

    # Find inode
    inode_blockStart = sblock[8]
    ninodes_in_block = Disk.BLOCK_SIZE//blocks.Inode.size
    inode_blockNum = inodeNum//ninodes_in_block
    real_blockNum = inode_blockNum + inode_blockStart
    inode_block = disk_blocks[real_blockNum]
    inode = inode_block[inodeNum*blocks.Inode.size:(inodeNum+1)*blocks.Inode.size]

    # Make changes to Inode
    inode[0] = blocks.Inode.DIR
    inode[2] = dentry

    # Add Data Bitmap to buffer
    data_bitmap = BlockBitMap(Disk.BLOCK_SIZE, 1)
    data_bitmap.blockBitMap = disk_blocks[1]
    data_bitmap.setUsed(0)  # Mark data block as used
    disk_blocks[1] = data_bitmap.saveToDisk()

    # Find datablock
    data_blockStart = sblock[7]
    data_block = disk_blocks[data_blockStart]

    # Change data block


    pass

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

# Have to read the whole file and rewrite it to disk because of how python works
def add_disk_to_buffer(open_file):
    sblock = Disk.disk_read(open_file, 0)  #read superblock to determine number of blocks on disk
    nblocks = sblock[1]
    disk_blocks = np.zeros(shape=(nblocks, Disk.BLOCK_SIZE//4), dtype=Disk.CELLSIZE)

    for i in range(nblocks):
        disk_read = Disk.disk_read(open_file, i)
        disk_blocks[i] = disk_read
    
    return disk_blocks

def find_inode(inode_blockStart, ):
    pass