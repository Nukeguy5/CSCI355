
class Disk():
    DISK_BLOCK_SIZE = 4096 # change to any size but make sure it is the right increment
    
    def __init__(self, filename, nblocks = 100):
        self.filename = filename
        self.nblocks = nblocks
    
    def disk_open(self, filename):
        pass

    def disk_size(self):
        return self.nblocks
    
    def disk_read(self, blocknum):
        pass
    
    def disk_write(self, blocknum, data):
        pass

    def disk_close(self):
        pass
