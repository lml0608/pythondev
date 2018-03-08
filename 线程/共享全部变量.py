from threading import Thread

import time

g_num = 0
def work1():

    global g_num
    for i in range(1000000):
        #print(i)
        g_num += 1

    print("---in work1, g_num is %d--" % g_num)

def work2():
    global g_num
    for i in range(1000000):
        #print(i)
        g_num += 1

    print("---in work2, g_num is %d--" % g_num)


print("----线程创建之前g_num is %d---" % g_num)


t1 = Thread(target=work1)
t1.start()

time.sleep(5)


t2 = Thread(target=work2)

t2.start()
print("---g_num=%d--" % g_num)

'''全局变量在多线程共享'''