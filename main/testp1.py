
from memory.memmgmt import MemoryManagementA
from memory.memmgr import MemoryA
from process.processx import Process

p1 = Process(4)
p1.print_mgmt()

print(" ***** before loading ****")
MemoryA.print_mem()
MemoryManagementA.print_management()
print(" *************************")

alist = [0,1]
p1.load_pages(alist, 2)

print(" ***** after loading *****")
p1.print_mgmt()
MemoryA.print_mem()
MemoryManagementA.print_management()
print(" *************************")

# get vectors
vectorlist = p1.get_vectors()
nbr = 22
for v in vectorlist:
    for r in range(0,v.shape[0]):
        v[r] = nbr
    nbr += 11

print(" ***** modifying  ****")
MemoryA.print_mem()
print(" *********************")