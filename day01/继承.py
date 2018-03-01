# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

class base(object):

    def test(self):

        print('------base------')

class A(base):

    def test(self):
        print('----a----')

class B(base):

    def test(self):
        print('-----b---')

class C(A,B):

    pass



c = C()

c.test()

print(C.__mro__)

