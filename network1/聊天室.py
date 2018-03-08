# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from socket import *
from time import ctime

#创建Udp socket
udpSocket = socket(AF_INET,SOCK_DGRAM)

bindAddr = ('',7789)
udpSocket.bind(bindAddr)
#sendAddr = ('192.168.1.98',8085)

while True:
    # 接收对方发送的数据,1024表示本次接收的最大字节数
    recvData = udpSocket.recvfrom(1024)

    print('【%s】%s:%s' % (ctime(),recvData[1][0],recvData[0]))


#
# data = sendDate.encode(encoding="utf-8")

#udpSocket.sendto(data,sendAddr)





#print(recvData)
#.decode()

udpSocket.close()