# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


def makeBold(fn):

    def wrapeed():
        return "<b>" + fn() +"</b>"

    return wrapeed

def makeItalic(fn):

    def wrapeed():
        return "<i>" + fn() + "</i>"

    return wrapeed



@makeBold
def test1():

    return "hello world-1"

@makeItalic
def test2():
    return "hello world-2"


@makeBold
@makeItalic
def test3():

    return "hello world-3"

print(test1())

print(test2())
print(test3())

