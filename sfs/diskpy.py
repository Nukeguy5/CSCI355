
import numpy as np
# from threading import Lock

class Disk():
    DISK_BLOCK_SIZE = 16 # change to any size but make sure it is the right increment
    disk = []

    def __init__(self, disk_name, nblocks = 16):
        self.disk_name = disk_name
        self.nblocks = nblocks
        self.disk = np.zeros(shape=(nblocks, Disk.DISK_BLOCK_SIZE), dtype='int8')

        with open(disk_name, 'wb') as d:
                d.write(self.disk)

    @classmethod
    def disk_open(cls, disk_name):
        try:
            with open(disk_name, 'rb') as d:
                byte_list = []
                while True:
                    byte = d.read(1)
                    if not byte:
                        break
                    byte_list.append(byte)

                nblocks = len(byte_list)/Disk.DISK_BLOCK_SIZE
                ndisk = Disk(disk_name, int(nblocks))
                for i in range(ndisk.nblocks):
                    block = ndisk.disk_read(i)
                    ndisk.disk[i] = block

            return ndisk

        except FileExistsError:
            print("Disk does not exist.")

    def disk_size(self):
        return self.nblocks
    
    def disk_read(self, blocknum):
        assert(blocknum <= self.nblocks), "ERROR: Blocknum {} is too large.".format(blocknum)
        
        start_addr = blocknum*Disk.DISK_BLOCK_SIZE
        block_size = Disk.DISK_BLOCK_SIZE
        block_data = []  # List of binary data

        with open(self.disk_name, 'rb') as d:
            d.seek(start_addr)  # Start reading from this address
            for _ in range(block_size):
                byte = d.read(1)  # Read one byte of data at a time
                data = int.from_bytes(byte, byteorder='big')
                block_data.append(data)

        # # Convert from list of bytes to list of ints
        # block_data = list(map(lambda x: int.from_bytes(x, byteorder='little'), block_raw))
        return block_data
    
    def disk_write(self, blocknum, data):
        # Check length of data in the filesystem
        assert(blocknum <= self.nblocks), "ERROR: blocknum {} is too big".format(blocknum)

        # Check the data type to determine how to convert to binary
        if type(data) == str:
            data = bytearray(data, 'utf8')
        else:
            data = bytearray(data)

        with open(self.disk_name, 'wb') as d:
            self.disk[blocknum] = data
            d.write(self.disk)

    @classmethod
    def disk_close(self):
        pass


class SuperBlock():
    magicnum = 0
    nblocks = 0
    ninodeblocks = 0
    ninodes = 0

class Inode():
    pass

