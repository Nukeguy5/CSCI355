
from memmgr import MemMgr
from memory.memmgmt import MemMgmt
import memory.memerror as me
# import memory.memcommon as mc
import traceback

def change_contents(array, value):
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = value


try:
    MemMgr.get_mem(222, 3)
    MemMgr.display_mem()
    MemMgmt.display_mgmt()

    MemMgr.get_mem(333, 2)
    MemMgr.display_mem()
    MemMgmt.display_mgmt()

    MemMgr.get_mem(444,1)
    MemMgr.display_mem()
    MemMgmt.display_mgmt()

    MemMgr.release_mem(333)
    MemMgr.display_mem()
    MemMgmt.display_mgmt()

    # a4 = MemMgmt.get_mem(555,3)
    # MemMgr.display_mem()
    # MemMgmt.display_mgmt()

except me.NOMEMORY:
    print("Memory error caught ************")
    traceback.print_exc()
    print("*************************")