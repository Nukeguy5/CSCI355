
import numpy as np
from diskpy import Disk
CELLSIZE = 'int32'

class Superblock:
    
    @classmethod
    def make_block(cls, nblocks=64, ninodeblocks=6, ninodes=32, dentry=0, dataBlock_bitmap=1, inode_bitmap=2, dataBlock_start=9, inodeBlock_start=3):
        arr = np.zeros(shape=(Disk.BLOCK_SIZE), dtype=CELLSIZE)
        arr[0] = 123456
        arr[1] = nblocks
        arr[2] = ninodeblocks
        arr[3] = ninodes
        arr[4] = dentry  # points to the directory inode
        arr[5] = dataBlock_bitmap
        arr[6] = inode_bitmap
        arr[7] = dataBlock_start
        arr[8] = inodeBlock_start
        return arr


class Inode:

    size = 32  # logical size of inode data in bytes
    NOT_VALID = 0
    FILE = 1
    DIR = 2

    # returns a bytearray
    @classmethod
    def make_inode(cls, is_valid=NOT_VALID, direct_blocks=[0]*5, indirect_loc=0):
        block = np.zeros(shape=(Inode.size), dtype=CELLSIZE)
        block[0] = is_valid
        block[1] = Inode.size
        index = 0
        for i in range(2, len(direct_blocks)):
            block[i] = direct_blocks[index]
            index += 1
        block[2 + len(direct_blocks)] = indirect_loc
        return block


class InodeBlock:
    
    # consists of 128 Inodes
    @classmethod
    def make_block(cls):
        num_inodes = Disk.BLOCK_SIZE//Inode.size
        merged_inodes = np.zeros(shape=(Disk.BLOCK_SIZE), dtype=CELLSIZE)
        inode = Inode.make_inode()
        index = 0
        for _ in range(num_inodes):
            for item in inode:
                merged_inodes[index] = item
                index += 1
        return merged_inodes
