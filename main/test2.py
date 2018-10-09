
from memory.memmgmt import MemoryManagementA
from memory.memmgr import MemoryA
from process.processx import Process

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
p1 = Process(4)
p1.load_pages([0,1], 2)
modify(p1)
printAll("1st process", p1)

# second process
p2 = Process(3)
p2.load_pages([0], 1)
modify(p2)
printAll("2nd process", p2)

# first process load_pages
p1.load_pages([2],1)
modify(p1)
printAll(" 1st process load", p1)

# second process load
p2.load_pages([1],1)
modify(p2)
printAll(" 2nd process load", p2)

# third process
p3 = Process(3)
p3.load_pages([0,1], 2)
modify(p3)
printAll("3rd process", p3)