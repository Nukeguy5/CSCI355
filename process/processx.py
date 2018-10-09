import numpy as np
import time
from memory.memmgmt import MemoryManagementA
from memory.memmgr import MemoryA

class Process:
    pid_counter = 11

    def __init__(self, initialNbrOfPages):
        self.page_table = np.zeros(shape=(initialNbrOfPages, 1), dtype='int64')
        self.page_frame_vectors = [0] * initialNbrOfPages

        # Set initial value to page table indexs to -1
        for i in range(self.page_table.shape[0]):
            self.page_table[i][0] = -1  # is marked available       

        self.available_space = initialNbrOfPages
        self.mypid = Process.get_pid()

    def load_pages(self, listOfPages, nbrPages):
        listPageFrameVector = MemoryA.get_mem(self.mypid, nbrPages)

        for i in range(0, len(listOfPages)):
            pageFrameIndex, vectora = listPageFrameVector[i] # vectora is a pointer to memory
            self.set_page_table(listOfPages[i], pageFrameIndex, vectora)

    # page is a pointer to a location in memory
    def set_page_table(self, page, pageFrameIndex, vectora): #change name later pls
        MemoryManagementA.set_mgmt(pageFrameIndex, self.mypid)

        # for each row of the page table 
        for i in range(self.page_table.shape[0]):
            if self.page_table[i][0] == -1:
                self.page_table[i][0] = pageFrameIndex
                self.page_frame_vectors[i] = vectora
                self.available_space += 1
                break

    def get_vectors(self):
        temp_list = []
        for row in range(len(self.page_frame_vectors)):
            if type(self.page_frame_vectors[row]) != int:
                temp_list.append(self.page_frame_vectors[row])
        
        return temp_list

    def print_mgmt(self):
        for i in range(self.page_table.shape[0]):
            print('{} : {}  {}'.format(i, self.page_table[i], self.page_frame_vectors[i]))

    def get_my_pid(self):
        return self.mypid

    @classmethod
    def get_pid(cls):
        aa = Process.pid_counter
        Process.pid_counter += 23
        return aa


# temp = np.zeros(shape=(3, 6), dtype='int64')
# print(temp)
# obj = Process(3)
# obj.load_pages(temp, 3)

'''
1) Why do we send 'vectora' to setx()
2) What is the point of the pid
3) What are the actual steps of this process
4) Does setx just put the data into self.logPhyMgt
'''