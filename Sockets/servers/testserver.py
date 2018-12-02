import socket

# Server
r = socket.socket()
r.bind(('', 23456))
print("socket binded")
r.listen(1)
rconn, (ip, port) = r.accept()

while True:
    msg = rconn.recv(1024).decode('utf-8')
    if msg == 'test':
        print('Msg recieved')
        rconn.send(bytes('server: msg recieved', 'utf-8'))
    elif msg == 'connect back':
        s = socket.socket()
        msg = rconn.recv(1024).decode('utf-8')
        if msg == 'ready':
            s.connect(('127.0.0.1', 23457))
            print("connected")
            s.send(bytes("server: connected to client server", 'utf-8'))
            s.close()
