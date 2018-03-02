# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

'''被装饰的函数有参数
'''
from time import ctime,sleep

def timefun(func):

    def wrapedfunc(a,b):

        print("%s called at %s" % (func.__name__, ctime()))
        print(a,b)
        func(a,b)

    return wrapedfunc

@timefun
def foo(a,b):

    print(a+b)

foo(3,5)

sleep(5)

foo(5,7)