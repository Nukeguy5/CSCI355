# TODO: Make numpy array shareable memory

from multiprocessing import Process, Value, Array, sharedctypes
import os 
import numpy as np

column_size = 8
row_size = 4
global memaa
memaa = np.empty(shape=(row_size, column_size), dtype='int8')

# Added
def convert_npArray(np_arr):
    arr = []
    for np_row in np_arr:
        row = sharedctypes.RawArray('b', np_row)
        arr.append(row)

    return arr

def modifyprint(arr, vv):
    # np_arr = np.asarray(arr)  # Added
    rsize = arr.shape[0]
    csize = arr.shape[1]
    
    for r in range(rsize):
        for c in range(csize):
            arr[r,c] = vv

    print("[", os.getpid(), "] --------")
    print(arr)
    print()
    print(memaa)
    print()

def f(arr, va):
    modifyprint(arr, va)

if __name__ == '__main__':
    print(memaa)
    viewa = memaa[0:2, :column_size]
    # s_memaa = convert_npArray(memaa)  # Added
    # s_memaa = sharedctypes.RawArray('B', memaa)

    modifyprint(viewa, 11)

    p = Process(target=f, args=(viewa, 22,))
    p.start()
    p.join()

    # memaa = np.asarray(s_memaa)
    print("back to main - print whole array")
    print(memaa)
