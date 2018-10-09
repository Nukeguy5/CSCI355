
import time
import threading

class CountdownThread(threading.Thread):

    def __init__(self, acount):
        threading.Thread.__init__(self)
        self.count = acount

    def run(self):
        while self.count > 0:
            print(self.getName(), ": Counting down", self.count)
            self.count -= 1
            time.sleep(1)
        print("exit thread", self.getName())
        
        return
