

import time

start_time = time.time()

for a in range(0,1001):
    for b in range(0,1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a,b,c:%d,%d,%d" % (a,b,c))


#每台机器执行的总时间不同，基本运算数量大体相同

#主要关注最坏时间复杂度
end_time = time.time()

print("times:%d" % (end_time-start_time))

print("finished")