import time

from socket import *
udp = socket(AF_INET, SOCK_DGRAM)
udp.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
udp.bind(('', 1337)) # source
udp.setblocking(0)
udp.setsockopt(SOL_IP, IP_TTL, 4)
udp.connect(('127.0.0.1', 5006)) # destination

dump = "xxxxxxxxxxxxxxxxxxxxxx"

'''
for n in range (1,5):
   number = '0000000000000000000000' + str(n)
   length = len (number)
   user_data = number [(length-22):]
   udp.send(user_data)


for n in range (6,9):
   number = '0000000000000000000000' + str(n)
   length = len (number)
   user_data = number [(length-22):]
   udp.send(user_data)
'''


n=1
while 1:
   number = '0000000000000000000000' + str(n)
   length = len (number)
   user_data = number [(length-22):]
   udp.send(user_data)
   n=n+1
   time.sleep(0.00001)

#   if n > 4 :
#     break

'''
   mmmm = number [(length-5):]
   #print mmmm
   if mmmm == '00000':
     print n


'''
