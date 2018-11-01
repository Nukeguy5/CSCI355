
from diskpy import Disk
import time

# disk1 = Disk('disk1.bin', 16)
mydisk = None

def read_script(filename):
    with open(filename, 'r') as f:
        commands = f.readlines()

    for command in commands:
        command.replace('\n', '')
        command_parse(command)
        time.sleep(.5)

def command_parse(command):
    command = command.strip()
    clist = command.split(" ")
    global mydisk

    try:
        if clist[0] == 'disk_open':
            disk_name = clist[1]
            mydisk = Disk.disk_open(disk_name) 
        
        elif clist[0] == 'disk_read':
            blocknum = int(clist[1])
            print(mydisk.disk_read(blocknum))

        elif clist[0] == 'disk_write':
            blocknum = int(clist[1])
            data = ' '.join(clist[2:]) 
            print("Writing [", data, "] to disk...") 
            mydisk.disk_write(blocknum, data)

        elif clist[0] == 'disk_size':
            size = mydisk.disk_size()
            print(size)
        
        elif clist[0] == 'read_script':
            filepath = ' '.join(clist[1:])
            read_script(filepath)

        else:
            raise Exception("Command not found...")
    
    except AttributeError:
        print("No disk selected...")

def usage():
    # file = open_file('diskpy.py')
    print('\nCommands:')
    print('\tdisk_open <disk file path>')
    print('\tdisk_read <block number>')
    print('\tdisk_write <block number> <data to write>')
    print('\tdisk_size')
    print('\tread_script <script file path>')
    print('\texit')
    print()


if __name__ == '__main__':
    command = ''
    while True:
        usage()
        command = input('sfs > ')
        if command == 'exit':
            break
        command_parse(command)