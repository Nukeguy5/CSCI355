
import numpy as np

class MgmtA:
    mgmt = np.zeros(shape=(6,1), dtype='int32')

    @classmethod
    def find_free_space(cls, pid, nbrPages):
        start_row = 0  # indicates none
        end_row = 5
        # start the search from row 0
        found = False
        for i in range(start_row, end_row):
            if MgmtA.mgmt[i,0] == 0:
                # found the first row that is free
                # now check whether we have nbr rows free
                nbrx = i+nbrPages
                found = True
                try:
                    for x in range(i, nbrx):
                        if MgmtA.mgmt[x,0] == 0:
                            continue
                        else:
                            found = False
                            break
                except IndexError:
                    print("No memory left")

            if found:
                start_index = i
                end_index = i+nbrPages-1
                return start_index, end_index

        print("no memory left")  # no empty space
        
    @classmethod
    def set_x(cls, pageFrameIndex, pid):
        pass

    @classmethod
    def unset_x(cls, pageFrameIndex):
        pass

    @classmethod
    def print_mgmt(cls):
        print('------- Management Array -------')
        # pretty print to include index
        for r in range(0, 6):
            print(r, ' : ', MgmtA.mgmt[r, 0])
        print('--------------------------------\n')
