
'''

'''

from threading import Thread,enumerate

import time

def sing():

    for i in range(3):
        print("正在唱歌...%d" % i)

        time.sleep(1)

def dance():

    for i in range(3):
        print("正在跳舞...%d" % i)

        time.sleep(1)

if __name__=="__main__":

    print('---开始---:%s' %time.ctime())

    t1 = Thread(target=sing)
    t2 = Thread(target=dance)

    t1.start()
    t2.start()

    while True:
        length = len(enumerate())
        if length<=1:
            break
        print("2324")

        time.sleep(0.5)
