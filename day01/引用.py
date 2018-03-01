# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

# a = 1
# b = a
# a = 2
#
# print(a)#2
# print(b) #1

a = [1,2]

b = a

print(b)
a.append(3)
print(a)

print(b)

print(id(a))
print(id(b))


