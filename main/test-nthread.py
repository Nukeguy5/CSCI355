
from threadingx.nthread import CountdownThread

# Thread1 with count 10
t1 = CountdownThread(10)
t1.start()

# Thread2 with count 20
t2 = CountdownThread(20)
t2.start()

print("Exit main thread")