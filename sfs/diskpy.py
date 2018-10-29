
import numpy as np
from threading import Lock

class Disk():
    DISK_BLOCK_SIZE = 8 # change to any size but make sure it is the right increment
    DISK_LOCK = Lock()

    def __init__(self, filename, nblocks):
        self.filename = filename
        self.nblocks = nblocks
        self.disk = np.zeros(shape=(nblocks, Disk.DISK_BLOCK_SIZE), dtype='int16')
        self.DISK_LOCK = Disk.DISK_LOCK

    def disk_open(self, filename):
        with self.DISK_LOCK:
            with open(filename, 'wb') as f:
                f.write(self.disk)

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
        self.DISK_LOCK.release()


class Inode():
    pass

disk1 = Disk('disk1.bin', 16)
disk1.disk_open('disk1.bin')