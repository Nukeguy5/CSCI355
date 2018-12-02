# Import socket module 
import socket                
  
def sendCmd(socket, astr):
    str_bytes = bytes(astr,'utf-8')
    socket.send(str_bytes)
    ss = astr.split()

    # receive data from the server 
    if ss[0] == 'RETR':
        answer = socket.recv(1024).decode('utf-8')
        data_str = []
        
        while True:
            socket.timeout(1)
            data = socket.recv(1024).decode('utf-8')
            data_str.append(data)
        
        data = ''.join(data_str)
        with open(ss[1], 'w') as f:
            f.write(data)
    else:
        answer =  socket.recv(1024).decode('utf-8')

    print('server response: ', answer)

# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

sendCmd(s, 'LIST')
sendCmd(s, 'RETR somefile.txt')
sendCmd(s, 'STOR thisfile.bin')
sendCmd(s, 'SYSTEM')
sendCmd(s, 'QUIT')

# close the connection 
s.close()        