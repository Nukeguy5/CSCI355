import numpy as np

class MemMgr:
    row_size = 7
    column_size = 6
    mgmt_row_size = row_size
    mgmt_column_size = 1

    # memory array to represent memory we manage
    mem = np.zeros(shape=(row_size, column_size), dtype='int32')

    # management of memory - an array of process identifiers pid
    mgmt = np.zeros(shape=(mgmt_row_size, mgmt_column_size), dtype='int32')

    @classmethod
    def get_mem(cls, pid, nbrblocks):

        # Check for available memory
        free_mem, insert_idx = MemMgr.check_free_mem(nbrblocks)
        if nbrblocks > free_mem:
            raise MemoryError("Not enough memory available.")

        # Update Management table
        for i in range(nbrblocks):
            MemMgr.mgmt[insert_idx + i] = pid

        # Insert items into memory
        for r in range(nbrblocks):
            for c in range(MemMgr.column_size):
                MemMgr.mem[insert_idx + r][c] = pid
        return 0

    @classmethod
    def check_free_mem(cls, nbrblocks):
        free_mem = 0
        insert_idx = 0
        for r in range(MemMgr.mgmt_row_size):
            if MemMgr.mgmt[r] != 0 and free_mem < nbrblocks:
                free_mem = 0
                insert_idx = r + 1
            else:
               free_mem += 1
 
        return free_mem, insert_idx

    @classmethod
    def release_mem(cls, pid):
        for r in range(MemMgr.mgmt_row_size):
            if MemMgr.mgmt[r] == pid:
                MemMgr.mgmt[r] = 0

    @classmethod
    def display_mem(cls):
        print('--------- Memory Array ---------')
        for r in range(MemMgr.row_size):
            print(r, ':', MemMgr.mem[r])
        print('--------------------------------')
    
    @classmethod
    def display_mgmt(cls):
        print('---------- MGMT Array ----------')
        for r in range(MemMgr.row_size):
            print(r, ':', MemMgr.mgmt[r, 0])
        print('--------------------------------')
