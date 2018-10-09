import threading

x = 0  # shared object
counter = 10000000

# create a lock
x_lock = threading.Lock()

def addx():
    global x
    for i in range(counter):
        x_lock.acquire()
        x += 1
        x_lock.release()
    print('exit from addx')
    return

def subx():
    global x
    for i in range(counter):
        x_lock.acquire()
        x -= 1
        x_lock.release()
    print('exit from subx')
    return

# the test program
t1 = threading.Thread(target=addx)
t2 = threading.Thread(target=subx)

t1.start()
t2.start()

# wait for completion
t1.join()
t2.join()

print('value of x:', x)
print('exit from main thread')