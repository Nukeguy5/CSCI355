# TODO: Make numpy array shareable memory

from multiprocessing import Process, Value, Array, sharedctypes
import os 
import numpy as np

column_size = 8
row_size = 4
memaa = np.empty(shape=(row_size, column_size), dtype='int8')

def modifyprint(arr, vv):
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

    modifyprint(viewa, 11)

    p = Process(target=f, args=(viewa, 22,))
    p.start()
    p.join()

    print("back to main - print whole array")
    print(memaa)
