import numpy as np
import time

class MemoryManagementA:
    row_size = 7
    column_size = 2

    management = np.zeros(shape=(row_size, column_size), dtype='int32')

    @classmethod
    def set_mgmt(cls, pageFrameIndex, pid): # change name pls
        MemoryManagementA.sweep_decriment()
        MemoryManagementA.management[pageFrameIndex][0] = pid
        MemoryManagementA.management[pageFrameIndex][1] = 17

    @classmethod
    def unset_mgmt(cls, pageFrameIndex):
        #remove the pid cell to zero
        MemoryManagementA.management[pageFrameIndex][0] = -1
        MemoryManagementA.management[pageFrameIndex][1] = 0  # reset counter 

    # FIFO
    # @classmethod
    # def update_timestamp(cls):
    #     return time.time()

    @classmethod
    def find_free_space(cls, pid, nbrPages):
        free_space = MemoryManagementA.find_empty_idxs(nbrPages)

        if len(free_space) >= nbrPages:
            return free_space
            # => [0, 2, 3, ...] <- list of free memory indexs

        else:
            # remove oldest pid and return list of newly freed space
            free_space = MemoryManagementA.least_recently_used(nbrPages)
            return free_space
            # => [0, 2, 3, ...] <- list of free memory indexs

            # FIFO
            # free_space = MemoryManagementA.remove_oldest_pid()
            # enough_memory = False
            # while not enough_memory:
            #     # TODO: Use 'oldest_pid' to alert the pid that memory has been released
            #     # removed_pid_idxs, oldest_pid = MemoryManagementA.remove_oldest_pid()


            #     # in case the memory released is still not enough, we use free_space to store every released indexs 
            #     free_space += removed_pid_idxs

            #     # breaks loop once it has enough memory
            #     if len(free_space) >= nbrPages:
            #         enough_memory = True
            
            # return free_space
            # => [0, 2, 3, ...] <- list of free memory indexs

    @classmethod
    def find_pid_idxs(cls, pid):
        pid_idxs = []
        for i in range(len(MemoryManagementA.management)):
            current_pid = MemoryManagementA.management[i][0]
            if current_pid == pid:
                pid_idxs.append(i)

        return pid_idxs

    @classmethod
    def find_empty_idxs(cls, nbrPages):
        free_space = []
        for idx in range(MemoryManagementA.row_size):
            if len(free_space) == nbrPages:
                break
            elif MemoryManagementA.management[idx][0] == 0:
                free_space.append(idx)

        return free_space

    @classmethod
    def least_recently_used(cls, nbrPages):
        oldest_pid = MemoryManagementA.find_smallest_count()
        pid_idxs = MemoryManagementA.find_pid_idxs(oldest_pid)
        removed_idxs = MemoryManagementA.unset_oldest_pid(pid_idxs, nbrPages)
        enough_mem = False

        while not enough_mem:
            # TODO: Fix out of index problem when condition meant
            if nbrPages > len(removed_idxs):
                nbrPages -= len(removed_idxs)
                oldest_pid = MemoryManagementA.find_smallest_count()
                new_idxs = MemoryManagementA.find_pid_idxs(oldest_pid)
                pid_idxs = MemoryManagementA.unset_oldest_pid(new_idxs, nbrPages)               
            elif len(removed_idxs) < nbrPages:
                oldest_pid = MemoryManagementA.find_smallest_count()
                new_idxs = MemoryManagementA.find_pid_idxs(oldest_pid)
                removed_idxs = MemoryManagementA.unset_oldest_pid(new_idxs, nbrPages)            
            else:
                enough_mem = True
        
        return removed_idxs
    
    @classmethod
    def find_smallest_count(cls):
        smallest_count = 17
        for i in range(len(MemoryManagementA.management)):
            pid_counter = MemoryManagementA.management[i][1]
            if pid_counter < smallest_count:
                smallest_count = pid_counter
                pid = MemoryManagementA.management[i][0]

        return pid

    @classmethod
    def unset_oldest_pid(cls, pid_idxs, nbrPages):
        for i in range(nbrPages):
            MemoryManagementA.unset_mgmt(pid_idxs[i])
        
        return pid_idxs

    @classmethod
    def sweep_decriment(cls):
        for i in range(len(MemoryManagementA.management)):
            # if zero, do not decriment
            if MemoryManagementA.management[i][1] == 0:
                continue
            MemoryManagementA.management[i][1] -= 1

    # FIFO 
    # @classmethod
    # def find_oldest_pid(cls):
    #     oldest_timestamp = time.time()  # oldest_time is the current time for initial comparison
        
    #     for i in range(len(MemoryManagementA.management)):
    #         pid_timestamp = MemoryManagementA.management[i][1]
            
    #         # find the oldest timestamp
    #         # if the timestamps are the same, stick with the 1st one found
    #         if pid_timestamp < oldest_timestamp:
    #             oldest_timestamp = pid_timestamp
    #             pid = MemoryManagementA.management[i][0]  # get pid of oldest_timestamp
            
    #     return pid

    # @classmethod
    # def remove_oldest_pid(cls):
    #     oldest_pid = MemoryManagementA.find_oldest_pid()
    #     oldest_pid_idxs = MemoryManagementA.find_pid_idxs(oldest_pid)  # => indexs for oldest pid

    #     # remove oldest pid from indexs
    #     for pageFrameIndex in oldest_pid_idxs:
    #         MemoryManagementA.unset_mgmt(pageFrameIndex)

    #     return oldest_pid_idxs, oldest_pid

    @classmethod
    def print_management(cls):
        print('------------- management array -------------')
        for r in range(0, MemoryManagementA.row_size):
            print(r, ' : ', MemoryManagementA.management[r])
        print('--------------------------------------------')

    

#print(ManagementA.find_free_space(123, 3))