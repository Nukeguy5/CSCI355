
import numpy as np
from memory.mem_a9_24 import MemA

class ProcessX:
    pid_counter = 123
    
    @classmethod
    def get_pid(cls):
        aa = ProcessX.pid_counter
        ProcessX.pid_counter = ProcessX.pid_counter + 23
        return aa

    def __init__(self, initialNbrOfPages):
        self.tablePageFrame = np.zeros(shape=(initialNbrOfPages, 3), dtype='int64')
        self.tablePages = []
        self.mypid = ProcessX.get_pid()

    def get_vectors(self):
        alist = []
        rows = len(self.tableVector)
        

    def set_x(self, page, pageFrame, vectora):
        pass

    def load_pages(self, listOfPages, nbrOfPages):
        listPageFrameVector = MemA.get_mem(self.mypid, nbrOfPages)
        sizel = len(listOfPages) - 1
        for ii in range(0, sizel):
            pageFrame, vectora = listPageFrameVector[ii]
            self.set_x(listOfPages[ii], pageFrame, vectora)

    def print_process_mgmt(self):
        print('------- Process Management Array -------')
        for r in range(0, 6):
            print(r, ' : ', self.tablePages[r, 0])
        print('----------------------------------------\n')
