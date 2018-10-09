
import numpy as np
import memory.memerror as me
from memory.memcommon import MemCommon
from memmgmt import MemMgmt


class MemMgr:
    row_size = MemCommon.row_size               # max number of rows
    column_size = 6            # max number of columns

    # generate size of memory   
    mem = np.zeros(shape=(row_size,column_size), dtype='int32')
    
    @classmethod
    def get_mem(cls, pid, nbrblocks):
        
        assert(nbrblocks > 0),"[get_mem()] Number of blocks > 0"

        # find free space in memory
        start_index, end_index = MemMgmt.find_free_space(nbrblocks)

        # aa = MemMgr.mem[start_index:end_index+1, :MemMgr.column_size]
        
        #insert into memory
        MemMgr.set_memory(start_index, end_index, pid)

        # update the mgmt table
        MemMgmt.add_mgmt(start_index, end_index, pid)


        # return aa        # we did not check for errors. 
                        # Add error handling later.
                        # if the dimensions are not correct 
                        # get a ValueError - 
                        # use try except block

    @classmethod
    def release_mem(cls, pid):
        print('release_mem from pid ', pid)
        for r in range(0, MemMgmt.mgmt_row_size):
            if MemMgmt.mgmt[r,0] == pid:
                MemMgmt.mgmt[r,0] = 0
        return pid
    
    @classmethod
    def set_memory(cls, start_index, end_index, pid):
        for r in range(start_index,end_index + 1):
            for c in range(MemMgr.column_size):
                MemMgr.mem[r, c] = pid

    @classmethod
    def display_mem(cls):
        print('-------- Memory Array -------')
        for r in range(0, MemMgr.row_size):
            print(r, ' : ', MemMgr.mem[r, :MemMgr.column_size])
        print('-----------------------------\n')
