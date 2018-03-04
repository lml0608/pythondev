

import os
import time
g_num = 100


'''
全局变量在多个进程中不共享
'''

ret = os.fork()

if ret == 0:

    #子进程

    print("-----process-1--%d" % os.getpid())
    #print(g_num)

    g_num += 1

else:
    #父进程
    time.sleep(3)
    #print(g_num)
    print("-----process-2---%d" % os.getpid())

    ret = os.fork()

    if ret == 0:

        # 2儿子，子进程

        print("-----process-11--%d" % os.getpid())
        # print(g_num)

        g_num += 1

    else:

        #父进程
        time.sleep(3)
        # print(g_num)
        print("-----process-22--%d" % os.getpid())



