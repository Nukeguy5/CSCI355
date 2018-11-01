
from diskpy import Disk
import time

mydisk = None

def read_script(filename):
    with open(filename, 'r') as f:
        commands = f.readlines()

    for command in commands:
        command_parse(command)
        time.sleep(.5)

def command_parse(command):
    command = command.strip()
    clist = command.split(" ")
    global mydisk

    if clist[0] == 'select_disk':
        disk_name = clist[1]
        nblocks = int(clist[2])
        mydisk = Disk(disk_name, nblocks) 
    
    # elif mydisk == None:
    #     raise Exception('No disk selected.')

    elif clist[0] == 'disk_read':
        blocknum = int(clist[1])
        print(mydisk.disk_read(blocknum))

    elif clist[0] == 'disk_write':
        blocknum = int(clist[1])
        data = ''.join(clist[2:]) 
        print("Writing", data, "to disk...") 

    elif clist[0] == 'disk_size':
        size = mydisk.disk_size()
        print(size)
    
    # elif clist[0] == 'read_script':
    #     read_script(clist[1])

    else:
        raise Exception("Command not found...")


def usage():
    # file = open_file('diskpy.py')
    print('\nCommands:')
    print('\tselect_disk')
    print('\tdisk_read')
    print('\tdisk_write')
    print('\tdisk_size')
    # print('\t./ (read script)')
    print('\texit')


if __name__ == '__main__':
    command = ''
    while command != 'exit':
        command = input('sfs> ')
        command_parse(command)