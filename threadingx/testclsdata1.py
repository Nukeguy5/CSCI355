
import threading

class Aa(object):

    nn = 10000000
    lock = threading.Lock()
    x = 0

    @classmethod
    def addx(cls):
        with cls.lock:
            for i in range(cls.nn):
                cls.x += 1
        print('exit from addx')

    @classmethod
    def subx(cls):
        with cls.lock:
            for i in range(cls.nn):
                cls.x -= 1
        print('exit from subx')


threads = []
for func in [Aa.addx, Aa.subx]:
    threads.append(threading.Thread(target=func))
    threads[-1].start()

for thread in threads:
    thread.join()

print('value of x = ', Aa.x)
print('exit from main thread')
    