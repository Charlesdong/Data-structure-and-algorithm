#!/usr/bin/python           # This is server.py file

from time import ctime
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    data = c.recv(1024)
    print 'Got connection from', c, addr
    c.send('%s, %s'%(data, ctime()))
    c.close()                # Close the connection
