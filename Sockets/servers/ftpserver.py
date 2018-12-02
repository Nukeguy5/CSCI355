import socket			 
import os
from threading import Thread

cport = 12345

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print( " New thread started for "+ip+":"+str(port))

    def do_something(self, cmdstr):
        # split the string using white space as delimiter
        ss = cmdstr.split()
        cmd = ss[0]
        if len(ss) > 0:
            param = ''.join(ss[1:])
        return cmd, param, 'response to cmd: ' + cmd + ' is 45'

    def run(self):
        while True:
            aa = self.sock.recv(1024)
            aa_str = aa.decode('utf-8')
            print('received : ', aa_str)
            # expect this form: cmd a1 
        
            cmd, param, bb = self.do_something(aa_str)
            print('servicing cmd: ',cmd)

            if cmd == 'QUIT':     
                bb = 'Shutdown session'
            elif cmd == 'LIST':
                bblist = os.listdir('.')
                bb = ''
                for a1 in bblist:
                    bb += ' ' + a1
            elif cmd == 'RETR':
                ip = '127.0.0.1'
                connection = self.setupDataPort(ip)
                
                if connection:
                    try:
                        with open(param, 'r') as f:
                            # read = f.readlines() 
                            for line in f:
                                self.data_socket.send(bytes(line, 'utf-8'))
                        self.data_socket.close()
                        print("Data Socket Closed.")
                    except Exception as e:
                        self.data_socket.close()
                        print('Error:', e)
                        self.sock.send(bytes("FTP Connection closed due to error: %s" % e, 'utf-8'))
            elif cmd == 'STOR':
                pass 

            print('send response: ',bb)
            bb_bytes = bytes(bb, 'utf-8')
            self.sock.send(bb_bytes)
            if cmd == 'QUIT':
                self.sock.close()
                print('client thread ending')
                break

    def setupDataPort(self, ip):
        try:
            self.data_socket = socket.socket()
            port_str = self.sock.recv(1024).decode('utf-8')
            port_lst = port_str.split(' ')
            if port_lst[0] == 'PORT':
                self.dataport = int(port_lst[1])
                print("Connecting to", ip, "on port", self.dataport, "...")
                self.data_socket.connect((ip, self.dataport))
                print("Connection established to", ip, "on port", self.dataport)
                self.sock.send(bytes('server response: FTP Connection Established', 'utf-8'))
                return True
            
        except Exception as e:
            print('Error in setting data port:', e)
            return False


s = socket.socket()		 				
s.bind(('', cport))		 
print( "socket binded to %s" %(cport) )

# put the socket into listening mode 
s.listen(5)	 
print( "socket is listening")			
threads = [] # keep a list of threads so to do a join()

# wait for multiple clients to connect
while True:
    print('ftpserver waiting on accept')
    conn, (ip, port)  = s.accept()	# tuple of IP and Port of client
    print ('Got connection from ', ip, 'at port: ', port )
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)
    

for t in threads:
    t.join()
print('ftpserver is done')
     
    

