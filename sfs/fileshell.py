
from diskpy import Disk
import sfs
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
    command = command.lower()
    clist = command.split(" ")
    global mydisk

    try:
        if clist[0] == 'disk_open':
            filepath = ' '.join(clist[1:])
            print('\t' + 'Opening ' + filepath + ' ...')
            mydisk = Disk.disk_open(filepath)

        elif clist[0] == 'disk_create':
            disk_name = clist[1]
            nblocks = int(clist[2])
            Disk.disk_init(disk_name, nblocks)
        
        elif clist[0] == 'disk_read':
            blocknum = int(clist[1])
            print('\t', Disk.disk_read(mydisk, blocknum))

        elif clist[0] == 'disk_write':
            blocknum = int(clist[1])
            data = ' '.join(clist[2:]) 
            print("\tWriting '" + str(data) + "' to disk...")
            if blocknum != 0: 
                Disk.disk_write(mydisk, blocknum, data)
            else:
                print('\tERROR: Cannot write to Superblock...')

        # elif clist[0] == 'disk_size':
        #     size = mydisk.disk_size()
        #     total_bytes = size*Disk.DISK_BLOCK_SIZE
        #     print('\nDisk:', mydisk.disk_name)
        #     print('\tBlocks:', size)
        #     print('\tBytes:', total_bytes)
        #     print()
        
        elif clist[0] == 'disk_close':
            filepath = ' '.join(clist[1:])
            Disk.disk_close(filepath)

        elif clist[0] == 'fs_format':
            filepath = ' '.join(clist[1:])
            chk = input('Are you sure you would like to format the disk? (y/n)')
            chk = chk.lower()
            if chk == 'y':
                sfs.fs_format(filepath)
            else:
                print('\tFormat Canceled.')

        elif clist[0] == 'read_script':
            filepath = ' '.join(clist[1:])
            read_script(filepath)

        else:
            print("\t '" + command + "' is not a command...")
    
    except (AttributeError, IndexError):
        print('\tDisk not selected or invalid syntax...')

def usage():
    print('\nCommands:')
    print('\tdisk_create <new disk name> <number of blocks>')
    print('\tdisk_open <disk file path>')
    print('\tdisk_close <disk file path>')
    print('\tdisk_read <block number>')
    print('\tdisk_write <block number> <data to write>')
    # print('\tdisk_size')
    print('\tfs_format <disk file path>')
    print('\tread_script <script file path>')
    print('\texit')
    print()


if __name__ == '__main__':
    command = ''
    usage()
    while True:
        command = input('sfs> ')
        if command == 'exit':
            break
        command_parse(command)