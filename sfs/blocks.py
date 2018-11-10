
import numpy as np

CELLSIZE = 'int32'

class Superblock:
    
    @classmethod
    def make_block(cls, block_size, nblocks=5, ninodeblocks=4, ninodes=32):
        arr = np.zeros(shape=(block_size), dtype=CELLSIZE)
        arr[0] = 123456
        arr[1] = nblocks
        arr[2] = ninodeblocks
        arr[3] = ninodes
        arr[4] = 0  # points to the directory inode
        return arr


class Inode:

    size = 32 # logical size of inode data in bytes

    # returns a bytearray
    @classmethod
    def make_inode(cls, is_valid=False, direct_blocks=[0]*5, indirect_loc=0):
        arr = np.zeros(shape=(Inode.size), dtype=CELLSIZE)
        arr[0] = is_valid
        arr[1] = Inode.size  # find out what this is supposed to be
        index = 0
        for i in range(2, len(direct_blocks)):
            arr[i] = direct_blocks[index]
            index += 1
        arr[2 + len(direct_blocks)] = indirect_loc
        return arr


class InodeBlock:
    
    # consists of 128 Inodes
    @classmethod
    def make_block(cls, block_size):
        num_inodes = int( block_size / Inode.size)
        merged_inodes = np.zeros(shape=(block_size), dtype=CELLSIZE)
        inode = Inode.make_inode()
        index = 0
        for _ in range(num_inodes):
            for item in inode:
                merged_inodes[index] = item
                index += 1
        return merged_inodes


class IndirectBlock:

    # consists of 1024 4-byte pointers that point to data blocks
    def __init__(self, ):
        pass


class DataBlock:
    def __init__(self, ):
        pass


# print('Superblock: ', Superblock.make_block())
# print('Inode: ', Inode.make_inode())
# print('Inode Block: ', InodeBlock.make_block())
