
from memory.memmgmt import MemoryManagementA
from memory.memmgr import MemoryA
from process.processx import Process
import threading
import time

def modify(px):
    nbr = px.get_my_pid()
    vectorlist = px.get_vectors()

    for v in vectorlist:
        for r in range(0,v.shape[0]):
            v[r] = nbr
    

def printAll(astring, process):
    print(" ********* start: ", astring, '*********')
    process.print_mgmt()
    MemoryA.print_mem()
    MemoryManagementA.print_management()
    print(" *********** end: ", astring, '***********\n')


# first process
def p1thread():
    p1 = Process(4)
    p1.load_pages([0,1], 2)
    modify(p1)
    printAll("first process p1", p1)
    time.sleep(2)
    p1.load_pages([2], 1)
    printAll("load more pages p1", p1)
    return

# second process
def p2thread():
    p2 = Process(3)
    p2.load_pages([0], 1)
    modify(p2)
    printAll("second process p2", p2)
    time.sleep(2)
    p2.load_pages([1], 1)
    printAll("load more pages p2", p2)
    return

# third process load_pages
def p3thread():
    p3 = Process(3)
    p3.load_pages([0,1], 2)
    modify(p3)
    printAll("third process p3", p3)
    # time.sleep(2)
    # p3.load_pages([2], 1)
    return

# fourth process load
def p4thread():
    p4 = Process(4)
    p4.load_pages([0, 1], 2)
    modify(p4)
    printAll("fourth process p4", p4)
    return

t1 = threading.Thread(target=p1thread, args=())
t1.start()
# t1.join()

t2 = threading.Thread(target=p2thread, args=())
t2.start()
# t2.join()

t3 = threading.Thread(target=p3thread, args=())
t3.start()
# t3.join()

t4 = threading.Thread(target=p4thread, args=())
t4.start()
# t4.join()
