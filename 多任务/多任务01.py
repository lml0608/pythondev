import os
import time
ret = os.fork()
print(ret)

print("hhaa")

if ret==0:
    while True:

        print("-----子进程---%d" % os.getpid())
        time.sleep(5)
else:
    while True:

        print("-----父进程---%d" % os.getpid())
        time.sleep(5)
