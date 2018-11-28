
from diskpy import Disk
from blockbitmap import BlockBitMap
import sfs
import time

mydisk = None

def read_script(filename):
    with open(filename, 'r') as f:
        commands = f.readlines()

    for command in commands:
        command.replace('\n', '')
        if command[0] == '#':
            continue
        command_parse(command)
        time.sleep(.5)

def command_parse(command):
    command = command.strip()
    command = command.lower()
    clist = command.split(" ")
    global mydisk

    try:
        if clist[0] == 'disk_open':
            filepath = ' '.join(clist[1:])
            print('\t' + 'Opening ' + filepath + ' ...')
            mydisk = Disk.disk_open(filepath)

        elif clist[0] == 'disk_init':
            disk_name = clist[1]
            nblocks = int(clist[2])
            print("Initializing Disk {}...".format(disk_name))
            Disk.disk_init(disk_name, nblocks)
            print(disk_name, 'initialized.')
        
        elif clist[0] == 'disk_read':
            blocknum = int(clist[1])
            if len(clist) == 3:
                # try:
                bit32 = bool(clist[2])
                
                print(Disk.disk_read(mydisk, blocknum, bit32))
            else:
                print(Disk.disk_read(mydisk, blocknum))

        elif clist[0] == 'disk_write':
            blocknum = int(clist[1])
            data = ' '.join(clist[2:]) 
            print("\tWriting '" + str(data) + "' to disk...")
            if blocknum != 0: 
                Disk.disk_write(mydisk, blocknum, data)
            else:
                print('\tERROR: Cannot write to Superblock...')

        elif clist[0] == 'disk_close':
            filepath = ' '.join(clist[1:])
            Disk.disk_close(filepath)

        elif clist[0] == 'fs_format':
            filepath = ' '.join(clist[1:])
            chk = input('Are you sure you would like to format the disk? (y/n) ')
            chk = chk.lower()
            if chk == 'y':
                sfs.fs_format(filepath)
            else:
                print('\tFormat Canceled.')

        elif clist[0] == 'fs_findfree':
            if clist[1] == 'data':
                free_space_data = sfs.fs_findfree(mydisk, 1)
                print(free_space_data)
            elif clist[1] == 'inode':
                free_space_inode = sfs.fs_findfree(mydisk, 2) 
                print(free_space_inode)
            else:
                print("\tInvalid Bitmap...")
                print("\tUse 'data' or 'inode'")

        elif clist[0] == 'read_script':
            filepath = ' '.join(clist[1:])
            print('Executing...')
            read_script(filepath)

        elif clist[0] == 'dir':
            print('\troot/')

        elif clist[0] == 'cmds':
            usage()

        else:
            print("\t'" + command + "' is not a command...")
            print("\tUse 'cmds' to display list of commands")
    
    except (AttributeError, IndexError):
        usage()
        print('\tNo Disk selected or Invalid syntax...\n')
        return

def usage():
    print('\nCommands:')
    print('\tcmds')
    print('\tdir')
    print('\tdisk_init <new disk name> <number of blocks>')
    print('\tdisk_open <disk file path>')
    print('\tdisk_close <disk file path>')
    print('\tdisk_read <block number> <bit32? (default is False)>')
    print('\tdisk_write <block number> <data to write>')

    print('\tfs_format <disk file path>')
    print('\tfs_findfree <bitmap>')
    print('\tread_script <script file path>')
    print('\texit')
    print()


if __name__ == '__main__':
    command = ''
    while True:
        command = input('sfs> ')
        if command == 'exit':
            break
        command_parse(command)