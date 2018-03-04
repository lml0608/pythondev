from multiprocessing import Process

import time
import random

def test():

    for i in range(random.randint(1,5)):
        print("--%d---" % i)

        time.sleep(1)

p = Process(target=test)

p.start()

#time.sleep(5)
#join等待子进程结束后才会往下走
p.join(2)#堵塞

print("---main---")