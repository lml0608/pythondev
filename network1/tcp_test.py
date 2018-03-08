# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from socket import *

tcpSerSocket = socket(AF_INET, SOCK_STREAM)

address = ('',7788)

tcpSerSocket.bind(address)

tcpSerSocket.listen(5)

newSocket, clientAddr = tcpSerSocket.accept()

recvData = newSocket.recv(1024)

print(recvData)

newSocket.send("thank you!".encode(encoding="utf-8"))

newSocket.close()

tcpSerSocket.close()

