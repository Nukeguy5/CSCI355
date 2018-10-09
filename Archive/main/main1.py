import os, sys

sys.path.insert(1, os.path.join(sys.path [0], '..'))
print(sys.path)  # to show the path

# import test1
from memory.test1 import printString

printString("a call from main1")
