# send_file
Simple client-server based TCP file transfer service with implemented Diffie Hellman key exchange and simple Fernet symetric key encryption.
## Usage
1. Start the server on the system you want the files sent:
```
# python3 server.py
```
2. Then open the the send_file.py and add the servers IP and PORT under `SOCKET CONSTANTS`:
```
IP          = <SERVER IP>
PORT        = <SERVER PORT>
```
NOTE: I am going to add arguments in the near future so these variables are passed as command line arguments<br><be>

3. Start the send_file.py on the sending system:
```
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
