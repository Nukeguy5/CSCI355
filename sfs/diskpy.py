
import numpy as np
from threading import Lock

class Disk():
    DISK_BLOCK_SIZE = 8 # change to any size but make sure it is the right increment
    DISK_LOCK = Lock()

    def __init__(self, filename, nblocks):
        self.filename = filename
        self.nblocks = nblocks
        self.disk = np.zeros(shape=(nblocks, Disk.DISK_BLOCK_SIZE), dtype='int32')

    def disk_open(self, filename):
        Disk.DISK_LOCK.acquire()

    def disk_size(self):
        # print("Disk size:", self.nblocks*Disk.DISK_BLOCK_SIZE, "bytes")
        # print("Number of blocks on disk:", self.nblocks)
        return self.nblocks
    
    def disk_read(self, blocknum):
        try:
            return self.disk[blocknum]
        except IndexError:
            print("ERROR: blocknum", blocknum, "is too big")
    
    def disk_write(self, blocknum, data):
        try:
            self.disk[blocknum] = data
        except IndexError:
            print("ERROR: blocknum", blocknum, "is too big")

    def disk_close(self):
        Disk.DISK_LOCK.release()


# class Inode():
#     offset =     
#     pass