import socket

# Client
def sendCmd(sock, astr):
    sock.send(bytes(astr, 'utf-8'))
    
    if astr == 'connect back':
        r = socket.socket()
        r.bind(('', 23457))
        print("socket binded")
        r.listen(1)
        sock.send(bytes('ready', 'utf-8'))
        rconn, (ip, port) = r.accept()
        print("connected to", ip, "on port", port)
        msg = rconn.recv(1024).decode('utf-8')
        print(msg)
        rconn.close()

s = socket.socket()
s.connect(('127.0.0.1', 23456))
sendCmd(s, 'test')
msg = s.recv(1024).decode('utf-8')
print(msg)
sendCmd(s, 'connect back')
s.close()