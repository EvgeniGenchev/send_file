# send_file
Simple client-server based TCP file transfer service with Diffie Hellman key exchange implementation and Fernet symetric key encryption.<br>
![image](https://user-images.githubusercontent.com/59848681/121398010-3398ff00-c955-11eb-93b2-c490d2120c68.png)

<br>
## Requirements
- Python3.x
- cffi==1.14.5
- cryptography==3.4.7
- progress==1.5
- pycparser==2.20
- pyfiglet==0.8.post1

## Usage
1. Start the server on the system you want the files sent:
```bash
$ sudo python3 server.py <PORT>
```
2. Then open the the send_file.py and add the servers IP and PORT under `SOCKET CONSTANTS`:
```bash
IP          = <SERVER IP>
PORT        = <SERVER PORT>
```
NOTE: I am going to add arguments in the near future so these variables are passed as command line arguments<br><be>

3. Start the send_file.py on the sending system:
```bash
$ python3 send_file.py <Path/to/file>
```
4. Your file can be found in `output`
```
send_file
-> send_file.py
-> server.py
-> output
    -> <YOUR FILE> 
```
## What to expect
- RSA Encryption
- multiple files support
- flags and arguments implementation
- threading and multiclient support
- compiled binaries
