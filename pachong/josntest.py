# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


import json

strList= '[1,2,3,4]'

strDict = '{"city":"北京","name":"狗狗"}'

list1 = json.loads(strList)

dict1 = json.loads(strDict)

print(list1)
print(dict1)