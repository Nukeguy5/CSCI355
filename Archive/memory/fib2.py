import time
# Start Timer
startTime = time.time() 
def fib(n):
        # Fibbonaci Sequence starts at 1 so we will need to add two 1's later
        result = 1
        last = 1
        i = 2 # Counter starts at 2 since we are starting from the 2 number in sequence
        while i < n:
            # new result => old result + last
            # last => last result 
            result, last = result + last, result
            # Counter 
            i += 1  
        return result
print(fib(10))
# Stop Timer
stopTime = time.time() 
print("Time elapsed: ", stopTime - startTime)
