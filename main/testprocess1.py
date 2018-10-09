import numpy as np
import sys
sys.path.append('/Users/quentincurteman/Google Drive File Stream/My Drive/William Jessup/Fall 2018/Operating Systems/CS355')

from memory.memmgmt import MemoryManagementA
from memory.memmgr import MemoryA
from process.processx import Process

pp = Process(4)

print('***** before loading *****')
pp.print_mgmt()
MemoryA.print_mem()
MemoryManagementA.print_management()
print('**************************')

alist = [0,1]
pp.load_pages(alist, 2)

print('***** after loading *****')
pp.print_mgmt()
MemoryA.print_mem()
MemoryManagementA.print_management()
print('**************************')