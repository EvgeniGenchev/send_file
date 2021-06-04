import socket
import os 

IP     		= ""
PORT   		= 420
ADDR   		= (IP, PORT)
FORMAT 		= 'utf-8'
SIZE   		= 1024


def get_fns(msg):
    fn, fs = msg.decode(FORMAT).split(':')
    return fn, int(fs)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(ADDR)
    s.listen(5)

    while True:
        c, addr = s.accept()
        print(f"{addr} connected")
        
        filename, f_size = get_fns(c.recv(SIZE))
        
        print(filename, f_size)
        with open(filename, 'wb') as f:
            c.send(b"k")
            data = b""
            while not f_size < 0:
                if r  := c.recv(SIZE):
                    data += r
                f_size -= 1

            f.write(data)

        print(os.path.getsize(filename))

        
