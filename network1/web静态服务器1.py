# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import socket

from multiprocessing import Process

def handleClient(clientSocket):

    recvData = clientSocket.recv(2048)

    requestHeaderLines = recvData.splitlines()

    for line in requestHeaderLines:

        print(line)
    responseHeaderLines = "HTTP/1.1 200 OK\r\n"
    responseHeaderLines += "\r\n"
    responseBody = "hello world"
    response = responseHeaderLines + responseBody
    clientSocket.send(bytes(response, "utf-8"))
    clientSocket.close()





def main():

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    serverSocket.bind(("",7788))

    serverSocket.listen(10)


    while True:

        clientSocket, clientAddr = serverSocket.accept()

        clientP = Process(target = handleClient, args=(clientSocket,))

        clientP.start()

        clientSocket.close()



if __name__=='__main__':

    main()



