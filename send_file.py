import socket
import sys
import os
import random
import base64 
from time import sleep
from random import randint
from cryptography.fernet import Fernet

##############################
#   ENCRYPTION CONSTANTS     #
##############################

PUBLIC_KEY      = 59708570456722881330322593357104338966651446003343456336221467788120858294637612729468919641870893094553876418711331190252587603732951467619016010258393708614469014886630741052124859360041444193108422651091706806423767525717557549160937228475070461659036411796511031663726390826531579605910117065616694733668122400042761523035625538265054775408900368262501875230647412192849496154041649528018232677303594366464002058279455978918708071944566429865899400172540727701334068331171052954837693691485731956623707548164835534794749214152855138351307612740654402824438297751744610581477933728519783742375070530150526851016177643808258834449419771707976652376884373381958980430043083628600008436239689617948497848172637058229715789010162561091741961103841550627169196009879518890442756522616669795160167686941488985291643933286041977543413764650628033812509823163504995392106887720490752674166365827369227512170733209701186975194277257032069038050138970697957548923460863990408116746039077320121471185097127985944798620582169432985472880371975698652511029918101858806817737903033810916665335853624374293040960777822614803014973277813041650344328292238633606925550840199975886484341152143674603849202565645041269151238935780713757367987482890023963059585467418997199333044731891105970201737535066548350349211039172607845827851806296744001400452178125454562922949148577808408679424400935889291776890549328065327074550020058221328929762229804459599784369020891221383569037369359520013467945443730663145655838087889075756492211637788065964328941123526040892707880726390787720699815938123586561881795761125055828630484216794660990178267345009227174986171938418805753667180974996482147928293259663321979341912493835276483679934255086999768651997511889122983003823139759490038134443889882237674325463165228830086775738348359688440922103442707456707085688356406893419891378635361951978399776043653563612725111611824402853409810900713045142382676772923826840469763827166095880265935314675775725052333765712173441870668
  
PRIME           = 23
A               = int("".join([str(randint(0,9)) for _ in range(50)]))

##############################
#      SOCKET CONSTANTS      #
##############################

IP     		= "192.168.2.7"
PORT   		= 420
ADDR   		= (IP, PORT)
FORMAT 		= 'utf-8'
SIZE   		= 1024


##############################
#       FILE CONSTANTS       #
##############################

FILEPATH	= sys.argv[1]
FILENAME        = FILEPATH.split('/')[-1]
FILESIZE        = os.path.getsize(FILEPATH)
N               = 100

def auth(c):
    gAn = PRIME ^ A % PUBLIC_KEY
    gBn = int(c.recv(SIZE).decode(FORMAT))
    key = (gBn ^ A) % PUBLIC_KEY 

    sleep(0.1)
    c.send(str(gAn).encode(FORMAT))
    random.seed(key)
    
    key = "".join([chr(randint(33, 126)) for _ in range(32)])
    print(key)
    
    key = base64.urlsafe_b64encode(key.encode(FORMAT))
    
    fernet = Fernet(key)
    
    return fernet

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect(ADDR)

    fernet = auth(c)

    with open(FILEPATH, 'rb') as f:
        data = f.read()

    data = fernet.encrypt(data)
    
    data = [data[i:i+N] for i in range(0, len(data), N)]
    
    msg = FILENAME + ":" + str(len(data))
    print(FILESIZE)

    c.send(msg.encode(FORMAT))
    
    if c.recv(SIZE).decode(FORMAT) == 'k':
        print('prashtam')
        for d in data:
            c.send(d)

        
		

