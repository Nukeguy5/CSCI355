
import numpy as np
from diskpy import Disk

class BlockBitMap:

    def __init__(self, arraysize, blockNumber):
        self.blockNumber = blockNumber
        self.arraysize = arraysize
        self.blockBitMap = np.zeros(shape=(Disk.BLOCK_SIZE, 1), dtype='int8')

    def init(self):
        pass
    
    def setFree(self, offset):
        pass
    
    def setUsed(self, offset):
        pass
        
