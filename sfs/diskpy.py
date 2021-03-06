# import blocks
import numpy as np
import blocks

class Disk:

    BLOCK_SIZE = 16 # 4096

    # a row is a block
    @classmethod
    def disk_init(cls, diskname, nblocks=32):
        blank_blocks = np.zeros(shape=(nblocks, Disk.BLOCK_SIZE), dtype='int8')
        ninode_blocks = int(nblocks/10)  # Make 10% of blocks inodes
        sblock = blocks.Superblock.make_block(Disk.BLOCK_SIZE, nblocks, ninode_blocks)
        iblock = blocks.InodeBlock.make_block(Disk.BLOCK_SIZE)

        # Write initial blocks to array
        blank_blocks[0] = sblock
        for i in range(ninode_blocks):
            i += 1  # don't overwrite superblock
            blank_blocks[i] = iblock

        with open(diskname, 'wb') as f:
            f.write(blank_blocks)
            
    @classmethod
    def disk_open(cls, diskname):
        fl = open(diskname, 'rb+')
        return fl

    @classmethod
    def disk_read(cls, open_file, blockNumber):
        start_address = Disk.BLOCK_SIZE * blockNumber
        block_data = np.empty(shape=(1, Disk.BLOCK_SIZE), dtype='int8')

        open_file.seek(start_address)
        for i in range(Disk.BLOCK_SIZE):
             byte = open_file.read(1)
             block_data[0,i] = int.from_bytes(byte, 'little')

        return block_data

    @classmethod
    def disk_write(cls, open_file, blockNumber, data): 
        start_address = Disk.BLOCK_SIZE * blockNumber
        open_file.seek(start_address)
        byte_data = bytearray(data)       
        open_file.write(byte_data[:])

    @classmethod
    def disk_status(cls, ):
        print('The disk is doing GREAT!!')

    @classmethod
    def disk_close(cls, open_file):
        open_file.close()

# disk1 = Disk('qdisk.bin', 6)
# barr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# # disk1.disk_write(3, barr)
# # print(disk1.disk_read(3))


# Disk.disk_init('disk1.bin', 50)
# open_file = Disk.disk_open('disk1.bin')
# print(Disk.disk_read(open_file, 30))
# Disk.disk_write(open_file, 30, barr)
# print(Disk.disk_read(open_file, 30))
# print(Disk.disk_read(open_file, 31))
# print(Disk.disk_read(open_file, 32))
# print(Disk.disk_read(open_file, 33))
# Disk.disk_close(open_file)
