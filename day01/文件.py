# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

f = open('test.txt','r')
#f.write("你好，你睡睡。哈哈哈哈")

#a = f.read()

b = f.readlines()

print(type(b))

#print(len(b))

#print(a)


for line in b:
    print(line)

#print(b)

f.close()