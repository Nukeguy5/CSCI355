
import time
import threading

def countdown(aname, acount):
    while acount > 0:
        print(aname, ": Counting down", acount)
        acount -= 1
        time.sleep(1)
    print("exit thread", aname)

    return

t1 = threading.Thread(target=countdown, args=('t1', 10,))
t1.start()

t2 = threading.Thread(target=countdown, args=('t2', 20,))
t2.start()

print("Exit main thread")
