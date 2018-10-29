
from diskpy import Disk
import numpy as np
from threading import Lock

disk1 = Disk('disk1', 16)
fs_bitmap = np.zeros(shape=(disk1.disk_size(), 1), dtype='int32')
file_table = {}
fs_lock = Lock()

def fs_format():
    print("Formatting...")
    with fs_lock:
        for i in range(len(fs_bitmap)):
            fs_bitmap[i] = 0
    print("Format Complete.")

def fs_debug():
    print(' ------ Disk Mgmt -------')
    for i in range(len(fs_bitmap)):
        print(i, ':', fs_bitmap[i])
    print(' _______ End Mgmt _______')
    print()
    print(' --------- Disk ---------')
    for i in range(len(disk1.disk)):
        print(i, ':', disk1.disk[i])
    print(' _______ End Disk _______')
    print()

def fs_mount():
    pass

def fs_create():
    pass

def fs_delete(file):
    pass

def fs_getsize(file):
    pass

def fs_read(file, length, offset):
    with fs_lock:
        pass

def fs_write(file, data, length, offset):
    with fs_lock:
        fs_bitmap[offset] = 1
