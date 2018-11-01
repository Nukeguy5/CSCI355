
import numpy as np
from threading import Lock

class Disk():
    DISK_BLOCK_SIZE = 16 # change to any size but make sure it is the right increment

    def __init__(self, disk_name, nblocks):
        self.disk_name = disk_name
        self.nblocks = nblocks
        self.disk = np.zeros(shape=(nblocks, Disk.DISK_BLOCK_SIZE), dtype='int8')

        with open(self.disk_name, 'wb') as d:
            d.write(self.disk)

    def disk_open(self, filename):
        pass

    def disk_size(self):
        return self.nblocks
    
    def disk_read(self, blocknum):
        assert(blocknum <= self.nblocks), "ERROR: Blocknum {} is too large.".format(blocknum)
        
        start_addr = blocknum*Disk.DISK_BLOCK_SIZE
        block_size = Disk.DISK_BLOCK_SIZE
        block_raw = []  # List of binary data

        with open(self.disk_name, 'rb') as d:
            d.seek(start_addr)  # Start reading from this address
            for _ in range(block_size):
                data = d.read(1)  # Read one byte of data at a time
                block_raw.append(data)

        # Convert from list of bytes to list of ints
        block_data = list(map(lambda x: int.from_bytes(x, byteorder='little'), block_raw))
        return block_data
    
    def disk_write(self, blocknum, data):
        assert(blocknum <= self.nblocks), "ERROR: blocknum {} is too big".format(blocknum)

        # Check the data type to determine how to convert to binary
        if type(data) == str:
            data = bytearray(data, 'utf8')
        else:
            data = bytearray(data)

        with open(self.disk_name, 'r+b') as d:
            self.disk[blocknum] = data
            d.write(self.disk)

    def disk_close(self):
        pass


class SuperBlock():
    magicnum = 0
    nblocks = 0
    ninodeblocks = 0
    ninodes = 0

class Inode():
    pass

