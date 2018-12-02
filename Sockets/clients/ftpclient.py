# Import socket module 
import socket                
  
def sendCmd(socket, astr):
    str_bytes = bytes(astr,'utf-8')
    socket.send(str_bytes)
    ss = astr.split()

    # receive data from the server 
    if ss[0] == 'RETR':
        data_str = []
        
        data_port = 12346
        data_socket = createDataSocket(socket, data_port)
        answer = socket.recv(1024).decode('utf-8')

        print("Receiving Data...")
        while True:
            try:
                data_socket.settimeout(2)
                data = data_socket.recv(1024).decode('utf-8')
                print(data)
                data_str.append(data)
            except:
                break
        
        data_socket.close()
        print('Data Socket Closed.')
        saveFile(ss[1], data_str)
        
        
        data = ''.join(data_str)
        with open(ss[1], 'w') as f:
            f.write(data)
    else:
        answer =  socket.recv(1024).decode('utf-8')

    print('server response: ', answer)


def createDataSocket(control_sock, dataport):
    data_socket = socket.socket()
    data_socket.bind(('', dataport))
    print("socket binded to", dataport)
    data_socket.listen(1)
    print("socket is listening")
    control_sock.send(bytes("PORT %s" % dataport, 'utf-8'))
    print('ftpclient waiting on accept.')
    dsock, (ip, port) = data_socket.accept()
    print('Got connection from ', ip, 'at port: ', port)
    return dsock

def saveFile(filename, data):
    print('Saving file...')
    with open(filename, 'w') as f:
        f.seek(0)
        for item in data:
            f.write(item)
    print('File Saved.')

# Create a socket object 
s = socket.socket()          
    
# Define the control port 
cport = 12345

# connect to the server on local computer 
s.connect(('127.0.0.1', cport)) 

sendCmd(s, 'LIST')
sendCmd(s, 'RETR somefile.txt')
sendCmd(s, 'STOR thisfile.bin')
sendCmd(s, 'SYSTEM')
sendCmd(s, 'QUIT')

# close the connection 
s.close()        