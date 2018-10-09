# On MacOSX I had to open terminal, type "open .bash_profile" and then added the lines:
# 
# PYTHONPATH="/Users/nukeguy5/Desktop/Operating Systems - CSCI355:${PYTHONPATH}"
# export PYTHONPATH
# 
# I then restarted the debugger and tested and it ran


# This method works as well, but doesn't allow the directory to be accessed by all files
# import sys
# sys.path.append('/Users/nukeguy5/Desktop/Operating Systems - CSCI355/Code/memory')

from memory import test1

test1.print_string("here I am")
