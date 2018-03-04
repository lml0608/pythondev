# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


# x = 500 // 60
#
# y = 500 % 60
#
# print(x)
#
# print(y)

def getAverage(a,b):
    result = a + b

    print("result=%d" % result)

    return result


a = 100
b = 200

c = a + b

ret = getAverage(a,b)

print(ret)