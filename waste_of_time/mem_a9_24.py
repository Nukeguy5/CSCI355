
import numpy as np
from memory.memmgmt_9_24 import MgmtA

class MemA:
    mem = np.zeros(shape=(6,5), dtype='int8')

    @classmethod
    def get_mem(cls, pid, nbrPages):
        mem_list = []
        alist = MgmtA.find_free_space(pid, nbrPages)
            # returns list of pageFrames
            # if none, return an empty list
            
        if len(alist) > 0:
            for pageFrameIndex in alist:
                aa = MemA.mem[pageFrameIndex, :]
                tuplea = (pageFrameIndex, aa)
                mem_list.append(tuplea)
        return mem_list

    @classmethod
    def print_mem(cls):
        print('-------- Memory Array -------')
        for r in range(0, 6):
            print(r, ' : ', MemA.mem[r, :6])
        print('-----------------------------\n')
