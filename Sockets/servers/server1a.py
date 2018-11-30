# first of all import the socket library 
import socket			 
import os

# next create a socket object 
s = socket.socket()	

# current working directory
cwd = os.getcwd()

print( "Socket successfully created")

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345				

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))		 
print( "socket binded to %s" %(port) )

# put the socket into listening mode 
s.listen(5)	 
print( "socket is listening")			

# a forever loop until we interrupt it or 
# an error occurs 
counter = 0
while True: 

    # Establish connection with client. 
    counter += 1
    c, addr = s.accept()	 
    print ('Got connection from [', counter, '] ',addr )

    # send a thank you message to the client. 
    myname = socket.gethostname()
    myIP = socket.gethostbyname(myname)
    str = myname + '[' + myIP + '] : Thank you for connecting'
    c.send(bytes(str,'utf-8') )

    while True:
        cmd = c.recv(1024).decode('utf-8')
        if cmd == 'LIST':
            c.send(bytes(cwd, 'utf-8'))
        elif cmd == 'QUIT':
            print ('Connection closed from [', counter, '] ',addr )
            c.send(bytes('Closing...', 'utf-8'))
            break
    
    c.close()
