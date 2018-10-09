'''
This is what happens when you don't use locks. x will not equal zero 
because the functions are reading the numbers at the wrong time.
'''

import threading

x = 0
counter = 10000000

def addx():
    global x
    for i in range(counter):
        x += 1
    print('exit from addx')
    return

def subx():
    global x
    for i in range(counter):
        x -= 1
    print('exit form subx')
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