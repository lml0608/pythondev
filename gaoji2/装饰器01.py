# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from time import ctime,sleep

def timefun(func):

    def wrapedfunc():

        print("%s called at %s" % (func.__name__, ctime()))

        func()

    return wrapedfunc

@timefun
def foo():

    print("i am foo")

foo()

sleep(2)
foo()