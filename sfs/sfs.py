
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
    nblocks = sblock[1]
    ninode_blocks = sblock[2] 
    ninodes = sblock[3]
    dentry = 0
    dataBitmap_block = 1
    inodeBitmap_block = 2
    dataBlock_start = 3 + ninode_blocks
    inodeBlock_start = 3

    # TODO: Make more efficient to write empty data blocks to disk
    # Create buffer to write new data to disk
    blank_blocks = np.zeros(shape=(nblocks, Disk.BLOCK_SIZE), dtype='int8')
    sblock = blocks.Superblock.make_block(Disk.BLOCK_SIZE, nblocks, ninode_blocks, ninodes, dentry, dataBitmap_block, inodeBitmap_block, dataBlock_start, inodeBlock_start)
    iblock = blocks.InodeBlock.make_block(Disk.BLOCK_SIZE)
    
    # Create and initialize bitmaps
    data_bitmap = BlockBitMap(Disk.BLOCK_SIZE, dataBitmap_block)
    inode_bitmap = BlockBitMap(Disk.BLOCK_SIZE, inodeBitmap_block)
    ndata_blocks = nblocks - ninode_blocks - 3  # don't count super block or bitmaps
    data_bitmap.init(ndata_blocks)
    inode_bitmap.init(ninodes)
    inode_bitmap.blockBitMap[0] = BlockBitMap.BAD  # set inode 0 to BAD

    # Write initial blocks to array
    blank_blocks[0] = sblock
    blank_blocks[1] = data_bitmap.saveToDisk()
    blank_blocks[2] = inode_bitmap.saveToDisk()

    for i in range(ninode_blocks):
        i += 3  # don't overwrite superblock or bitmaps
        blank_blocks[i] = iblock
    
    Disk.disk_write(mydisk, 0, bytearray(blank_blocks))

    print("\tFormat Complete.")

def fs_debug():
    pass

def fs_mount():
    pass

def fs_create():
    pass

def fs_delete(file):
    pass

def fs_getsize(file):
    pass

def fs_read(file, length, offset):
    pass

def fs_write(file, data, length, offset):   
    pass
