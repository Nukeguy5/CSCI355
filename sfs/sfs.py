
from diskpy import Disk
import numpy as np
import blocks
from blockbitmap import BlockBitMap

# Disk.disk_init('disk1.bin', 16)
# fs_bitmap = np.zeros(shape=(Disk.nbrOfBlocks, 1), dtype='int32')

def fs_format(disk_name):
    print("\tFormatting...")

    # Read Super Block
    mydisk = Disk.disk_open(disk_name)
    sblock = Disk.disk_read(mydisk, 0)
    nblocks, ninode_blocks, ninodes = sblock[1], sblock[2], sblock[3]
    ndata_blocks = nblocks - ninode_blocks - 3  # don't count super block or bitmaps

    # Create buffer to write new data to disk
    blank_blocks = np.zeros(shape=(nblocks, Disk.BLOCK_SIZE), dtype='int8')
    sblock = blocks.Superblock.make_block(Disk.BLOCK_SIZE, nblocks, ninode_blocks)
    iblock = blocks.InodeBlock.make_block(Disk.BLOCK_SIZE)
    
    # Create and initialize bitmaps
    data_bitmap = BlockBitMap(Disk.BLOCK_SIZE, 1)
    inode_bitmap = BlockBitMap(Disk.BLOCK_SIZE, 2)
    data_bitmap.init(ndata_blocks)
    inode_bitmap.init(ninodes)


    # Write initial blocks to array
    blank_blocks[0] = sblock
    blank_blocks[1] = data_bitmap.blockBitMap
    blank_blocks[2] = inode_bitmap.blockBitMap

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

# Test
# fs_debug()
# string = 'testing this out.'
# fs_write('test.bla', string, len(string), 1)
# fs_debug()

