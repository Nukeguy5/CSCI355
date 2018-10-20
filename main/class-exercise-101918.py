
import multiprocessing as mp

def squared(q_do, q_result):
    nums = q_do.get()
    r_nums = []
    for i in nums:
        r_nums.append(i*i)
    q_result.put(r_nums)

def cubed(q_do, q_result):
    nums = q_do.get()
    r_nums = []
    for i in nums:
        r_nums.append(i*i*i)
    q_result.put(r_nums)

# Producer
if __name__ == '__main__':
    nums = [1,2,3,4]

    q_do = mp.Queue()
    q_result = mp.Queue()
    q_do.put(nums)
    q_do.put(nums)
    

    p1 = mp.Process(target=squared, args=(q_do,q_result))
    p2 = mp.Process(target=cubed, args=(q_do,q_result))

    p1.start()
    print(q_result.get())
    p2.start()
    print(q_result.get())
    p1.join()
    p2.join()

    