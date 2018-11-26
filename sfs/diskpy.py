
import numpy as np
# import blocks
from blockbitmap import BlockBitMap
import struct

class Disk:

    BLOCK_SIZE = 512 # 4096
    BYTEORDER = 'little'
    ENCODING = 'utf8'
    CELLSIZE = 'int32'

    # a row is a block
    @classmethod
    def disk_init(cls, diskname, nblocks=64):
        blank_blocks = np.zeros(shape=(nblocks, Disk.BLOCK_SIZE), dtype='int8')

        with open(diskname, 'wb') as f:
            f.write(bytearray(blank_blocks))
            
    @classmethod
    def disk_open(cls, diskname):
        fl = open(diskname, 'rb+')
        return fl

    @classmethod
    def disk_read(cls, open_file, blockNumber, bit32=False):
        start_address = Disk.BLOCK_SIZE * blockNumber
        
        open_file.seek(start_address)

        if not bit32:
            block_data = np.zeros(shape=(Disk.BLOCK_SIZE), dtype=Disk.CELLSIZE)
            for i in range(Disk.BLOCK_SIZE):
                byte = open_file.read(1)
                block_data[i] = int.from_bytes(byte, Disk.BYTEORDER)
        else:
            block_data = np.zeros(shape=(Disk.BLOCK_SIZE//4), dtype=Disk.CELLSIZE)
            for i in range(Disk.BLOCK_SIZE//4):
                byte_arr = open_file.read(4)
                block_data[i] = struct.unpack('i', byte_arr)[0]

        return block_data

    @classmethod
    def disk_write(cls, open_file, blockNumber, data): 
        start_address = Disk.BLOCK_SIZE * blockNumber
        open_file.seek(start_address)

        # Check the data type to determine how to convert to binary
        if type(data) == str:
            data_arr = np.zeros(shape=len(data), dtype='int8')
            for i in range(len(data)):
                char_val = bytes(data[i], Disk.ENCODING)
                data_arr[i] = int.from_bytes(char_val, Disk.BYTEORDER)
            byte_data = bytearray(data_arr)
        else:
            byte_data = bytearray(data)

        open_file.write(byte_data)

    @classmethod
    def disk_size(cls, open_file):
        open_file.seek(0, 2)
        size = open_file.tell() 
        return size

    @classmethod
    def disk_status(cls, ):
        print('The disk is doing GREAT!!')

    @classmethod
    def disk_close(cls, open_file):
        open_file.close()

# Disk.disk_init('disk1.bin')
