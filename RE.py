# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import re

# result = re.match("liubin","liubinnihao")

#
# x = result.group()
#
# print(type(x))#str
# print(x)

# #.匹配任何一个字符，不包括\n
# ret = re.match(".",'a')
# print(ret.group())
#
# ret = re.match(".",'c')
# print(ret.group())
#
# ret = re.match(".",'bet')
# print(ret.group()) #b

#[]  匹配[]中列举的字符
# 如果hello的⾸字符⼩写，那么正则表达式需要⼩写的h
# ret = re.match("h","hello Python")
# print(ret.group())
# # 如果hello的⾸字符⼤写，那么正则表达式需要⼤写的H
# ret = re.match("H","Hello Python")
# print(ret.group())
# # ⼤⼩写h都可以的情况
# ret = re.match("[hH]","hello Python")
# print(ret.group())
# ret = re.match("[hH]","Hello Python")
# print(ret.group())
#\d   匹配数字 0-9



#\D  匹配非数字
#\s  匹配空白，就是空格,tab键
#\S  匹配非空包
#\w 匹配单词字符，a-z,A-Z,0-9,_
#\W 匹配非单词字符

