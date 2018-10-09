from memory.mem_a9_24 import MemA
from memory.memmgmt_9_24 import MgmtA
from process.processx import ProcessX

# 12 pages initialized
p1 = ProcessX(4)
p1.print_mgmt()

print('************ before loading ***********')
MemA.print_mem()
MgmtA.print_mgmt()
print('***************************************')

alist = [0, 1]
p1.load_pages(alist, 2)

print('************* after loading ************')
p1.print_mgmt()
MemA.print_mem()
MgmtA.print_mgmt()
print('****************************************')

# now get those vectors
vectorlist = p1.get_vectors()
nbr = 22
for v in vectorlist:
    for r in range(0,v.shape[0]):
        v[r] = nbr
    nbr += 11

print('************** modifying ***************')
MemA.print_mem()
print('****************************************')
