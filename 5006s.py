### s-2 2016 0623, received and print
### s-3 2016 0624, verify process


import socket
import time
import datetime

port = 5006
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', port))
print "waiting on port:", port

seq = 1

while 1:
    data, addr = s.recvfrom(1024)

    client_seq = long(data)
    #print data, datetime.datetime.now(),"changed", client_seq
    if seq == client_seq :
        #print seq
        #print " "
        seq = seq + 1
    else:
        seq = client_seq + 1
        print "Missed clien_seq", client_seq
        print " "

    mm = data [17:]
    #print mm

    #print out per 100k
    if mm == "00000" :
        print "time = ", datetime.datetime.now()," SEQ = ", client_seq



