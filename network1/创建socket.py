# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''



'''
简称 套接字  进程间通信的一张方式，实现不同主机的进程间通信
创建
socket.socket(AddressFamily, Type)
 '''


import socket

#tpc
#AF_INET 用于Internet    AF_UNIX用于同一台机器进程间通信

#Type 套接字类型,SOCK_STREAM 流式套接字，主要用于TCP
#SOCK_DGRAM 数据报套接字，主要用于UDP


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s2 =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print(s)
print(s2)
