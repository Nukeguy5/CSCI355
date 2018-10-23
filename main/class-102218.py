
import multiprocessing as mp
import os, sys

class Dispatcher():

    def __init__(self):
        self.in_q = context


class Worker(mp.process):

    def __init__(self, inq, outq):
        self.inq = inq
        self.outq = outq


def controller(check):
    pass

def initialize():
    aa = [2,3,4,5]
    inq = [mp.]

if __name__ == '__main__':
    nums = [1,2,3,4]

    q_do = mp.Queue()
    q_result = mp.Queue()
    q_do.put(nums)
    q_do.put(nums)
    
    p1 = mp.Process()
    p2 = mp.Process()

    p1.start()
    print(q_result.get())
    p2.start()
    print(q_result.get())
    p1.join()
    p2.join()

    