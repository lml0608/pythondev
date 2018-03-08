# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from socket import *

#创建Udp socket
udpSocket = socket(AF_INET,SOCK_DGRAM)

bindAddr = ('',7788)
udpSocket.bind(bindAddr)
sendAddr = ('192.168.1.98',8085)


# udpClient.sendto(data, addr)  # 发送数据
# data, addr = udpClient.recvfrom(bufsize)  # 接收数据和返回地址
# print(data.decode(encoding="utf-8"), 'from', addr)
sendDate = input("请输入要发送的数据：")
data = sendDate.encode(encoding="utf-8")
udpSocket.sendto(data,sendAddr)



#接收对方发送的数据,1024表示本次接收的最大字节数
recvData = udpSocket.recvfrom(1024)

print(recvData)
#.decode()

udpSocket.close()