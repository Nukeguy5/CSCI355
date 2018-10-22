
import multiprocessing as mp

def selfSquared(num):
    print(mp.current_process().name, ":: number = ", num)
    return num*num

if __name__ == "__main__":
    print('cpu count = ', mp.cpu_count())
    numSequence = [31,53,79]
    pool = mp.Pool(processes=3)
    print(mp.current_process().name, ":: ", pool.map(selfSquared, numSequence))