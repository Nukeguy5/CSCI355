
import random, time
from threading import BoundedSemaphore, Thread

max_items = 5

# Container has a max limit of 5 items in this case
container = BoundedSemaphore(max_items)

def producer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(3, 5))
        print(time.ctime(), end=': ')
        try:
            container.release()
            print("Produced an item.")
        except ValueError:
            print("Full, Skipping.")

def consumer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(3, 5))
        print(time.ctime(), end=": ")

        if container.acquire(False):
            print("Consumed an item.")
        else:
            print("Empty, skipping.")

threads = []
nloops = random.randrange(1, 2)
print('Starting with %s itmes' % max_items)
threads.append(Thread(target=producer, args=(nloops,)))
threads.append(Thread(target=consumer, args=(random.randrange(nloops, nloops+max_items+2),)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
print('All done.')