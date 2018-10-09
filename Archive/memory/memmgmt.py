# import sys
import numpy as np
import memerror as me
from memory.memcommon import MemCommon


class MemMgmt:
    mgmt_row_size = MemCommon.row_size    # max number of rows for mgmt
    # mgmt_row_size = 7
    mgmt_column_size = 1        # max number of columns for mgmt
                                #  -- one column of pid
    pid_column = 0              # column for pid

    # management of memory - an array of process identifiers pid
    mgmt = np.zeros(shape=(mgmt_row_size,mgmt_column_size), dtype='int32')

    @classmethod
    def find_free_space(cls, nbr):
        start_row = 0  # indicates none
        end_row = MemMgmt.mgmt_row_size
        # start the search from row 0
        found = False
        for i in range(start_row, end_row):
            if MemMgmt.mgmt[i,0] == 0:
                # found the first row that is free
                # now check whether we have nbr rows free
                nbrx = i+nbr
                found = True
                try:
                    for x in range(i, nbrx):
                        if MemMgmt.mgmt[x,0] == 0:
                            continue
                        else:
                            found = False
                            break
                except IndexError:
                    raise me.NOMEMORY

            if found:
                start_index = i
                end_index = i+nbr-1
                return start_index, end_index

        raise me.NOMEMORY  # no empty space

    @classmethod
    def add_mgmt(cls, start_index, end_index, pid):
        for r in range(start_index, end_index+1):
            MemMgmt.mgmt[r, MemMgmt.pid_column] = pid

    @classmethod
    def display_mgmt(cls):
        print('------- Management Array -------')
        # pretty print to include index
        for r in range(0, MemMgmt.mgmt_row_size):
            print(r, ' : ', MemMgmt.mgmt[r, 0])
        print('--------------------------------\n')
