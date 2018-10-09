import numpy as np

from memory.memmgmt import MemoryManagementA

class MemoryA:
    row_size = 7
    column_size = 5

    memory = np.zeros(shape=(row_size, column_size), dtype='int8')

    @classmethod
    def get_mem(cls, pid, nbrPages):
        mem_list = []
        alist = MemoryManagementA.find_free_space(pid, nbrPages)  # returns a list of pageFrames
        
        if len(alist) > 0:
            for pageFrameIndex in alist:
                vectora = MemoryA.memory[pageFrameIndex, :]
                tuplea = (pageFrameIndex, vectora)  # vectora is a POINTER to memory
                mem_list.append(tuplea)
        return mem_list  # mem_list is a list of tuples
    
    @classmethod
    def print_mem(cls, ):
        print('--------------- memory array ---------------')
        for r in range(0, MemoryA.row_size):
            print(r, ' : ', MemoryA.memory[r])
        print('--------------------------------------------')
