
from diskpy import Disk
import numpy as np
from threading import Lock

disk1 = Disk('disk1.bin', 16)
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
    nblocks = disk1.nblocks
    for blocknum in range(nblocks):
        block_data = disk1.disk_read(blocknum)
        print(blocknum, ':', block_data)
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
    block_size = Disk.DISK_BLOCK_SIZE
    blocks = []

    def write_to_nblocks(data, offset):
        data_length = len(data)
        if data_length <= block_size:
            disk1.disk_write(offset, data)
            blocks.append(offset)
            return  

        data_remaining = data[block_size:data_length]
        data = data[:block_size]
        disk1.disk_write(offset, data)
        blocks.append(offset)
        offset += 1
        return write_to_nblocks(data_remaining, offset) 
    
    # Check length of data to determine if needs to be written to more blocks
    if len(data) > block_size:
        write_to_nblocks(data, offset)
    else:
        disk1.disk_write(data, offset)
        blocks.append(offset)

    # Make note in bitmap and file table
    for blocknum in blocks:
        fs_bitmap[blocknum] = 1
    file_table[file] = blocks

# Test
fs_debug()
string = 'testing this out.'
fs_write('test.bla', string, len(string), 1)
fs_debug()