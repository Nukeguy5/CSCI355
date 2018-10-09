
import time
import threading

def countdown(acount):
    while acount > 0:
        print("Counting down", acount)
        acount -= 1
        time.sleep(1)
    print("exit thread function")

    return

t1 = threading.Thread(target=countdown, args=(10,))
t1.start()
t1.join()  # waits for thread to exit before starting t2

t2 = threading.Thread(target=countdown, args=(20,))
t2.start()
t2.join()

print("Exit main thread")
