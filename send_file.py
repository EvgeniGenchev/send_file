import socket
import sys
import os
from time import sleep

IP     		= "192.168.2.7"
PORT   		= 420
ADDR   		= (IP, PORT)
FORMAT 		= 'utf-8'
SIZE   		= 1024
FILEPATH	= sys.argv[1]
FILENAME        = FILEPATH.split('/')[-1]
N               = 900

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect(ADDR)
    with open(FILEPATH, 'r') as f:
        data = f.read()
    
    data = [data[i:i+N] for i in range(0, len(data), N)]
    
    msg = FILENAME + ":" + str(len(data))
    print(len(data))

    c.send(msg.encode(FORMAT))
    
    if c.recv(SIZE).decode(FORMAT) == 'k':
        print('prashtam')
        for d in data:
            c.send(d.encode(FORMAT))

        
		

