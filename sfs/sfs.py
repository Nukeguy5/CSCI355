
from diskpy import Disk
import numpy as np
import blocks

# Disk.disk_init('disk1.bin', 16)
# fs_bitmap = np.zeros(shape=(Disk.nbrOfBlocks, 1), dtype='int32')
file_table = {}

def fs_format(disk_name):
    print("\tFormatting...")
    mydisk = Disk.disk_open(disk_name)
    sblock = Disk.disk_read(mydisk, 0)
    nblocks = sblock[0, 1]
    blank_blocks = np.zeros(shape=(nblocks, Disk.BLOCK_SIZE), dtype='int8')
    ninode_blocks = int(nblocks/10)  # Make 10% of blocks inodes
    sblock = blocks.Superblock.make_block(Disk.BLOCK_SIZE, nblocks, ninode_blocks)
    iblock = blocks.InodeBlock.make_block(Disk.BLOCK_SIZE)

    # Write initial blocks to array
    blank_blocks[0] = sblock
    for i in range(ninode_blocks):
        i += 1  # don't overwrite superblock
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