# -*- coding:utf-8 -*-
'''
__author__:liubin 

'''

from socket import *
from threading import Thread
from time import sleep

#处理客户端的请求并执行任务
def dealWithClient(newSocket, destAddr):

    while True:

        recvData = newSocket.recv(1024)

        if len(recvData) > 0:
            print('recv[%s]:%s' % (str(destAddr),recvData))

        else:

            print("[%s]客户端已经关闭" % str(destAddr))
            break


    newSocket.close()


def main():

    serSocket = socket(AF_INET, SOCK_STREAM)

    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    localAdr = ('', 7788)

    serSocket.bind(localAdr)

    serSocket.listen(5)

    try:
        print("---主进程，等待新客户端的到来----")

        newSocket, destAddr = serSocket.accept()

        print("---主线程，接下来创建一个新的进程负责数据处理[%s]-----" % str(destAddr))

        client = Thread(target=dealWithClient,args=(newSocket,destAddr))

        client.start()

    finally:
        serSocket.close()


if __name__=='__main__':

    main()

