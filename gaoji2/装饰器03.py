# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from time import ctime, sleep

'''被装饰的函数有不定长参数
'''
def timefun(func):
    def wrappedfunc(*args, **kwargs):
        print("%s called at %s"%(func.__name__, ctime()))

        print(args)
        func(*args, **kwargs)
    return wrappedfunc

@timefun
def foo(a, b, c):
    print(a+b+c)

foo(3,5,7)
sleep(2)
foo(2,4,9)