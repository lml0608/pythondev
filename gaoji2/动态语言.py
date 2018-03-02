# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


import types


class Person(object):

    num = 0

    def __init__(self,name = None,age = None):

        self.name = name
        self.age = age

    def eat(self):
        print("eat food")


def run(self,speed):
    print("%s在移动，速度是%d km/h" % (self.name,speed))



@classmethod
def testClass(cls):
    cls.num = 100

@staticmethod
def testStatic():
    print("----static method---")



p = Person("老王",34)

p.eat()

p.run = types.MethodType(run,p)

p.run(180)

#绑定类方法
Person.testClass = testClass
print(Person.num)

Person.testClass()
print(Person.num)


#绑定静态方法

Person.testStatic = testStatic
Person.testStatic()