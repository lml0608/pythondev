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

# ret = re.match("嫦娥1号","嫦娥1号发射成功")
# print(ret.group())
# ret = re.match("嫦娥2号","嫦娥2号发射成功")
# print(ret.group())
#
# ret = re.match("嫦娥\d号","嫦娥1号发射成功")
# print(ret.group())
# ret = re.match("嫦娥\d号","嫦娥2号发射成功")
# print(ret.group())


#\D  匹配非数字
#\s  匹配空白，就是空格,tab键
#\S  匹配非空包
#\w 匹配单词字符，a-z,A-Z,0-9,_
#\W 匹配非单词字符

# mm = "c:\\a\\b\\c"
# print(mm)
# print(re.match(r"c:\\a",mm).group())


#*  匹配前一个字符出现0次或无限次

# ret = re.match("[A-Z][a-z]*","Mneret")
#
# print(ret.group())
#+  匹配前一个字符出现1次或无限次

#匹配字符出现1次或无限次，匹配单词字符，a-z,A-Z,0-9,_出现0次或无限次
# ret = re.match("[a-zA-Z]+[\w]*","name1me_")

# print(ret.group())
#?     匹配前一个字符出现1次或0次

# ret = re.match("[1-9]?[0-9]","09")
#
# print(ret.group())
#{m} 匹配前一个字符出现m次
# ret = re.match("[a-zA-Z0-9]{6,20}","2423242rwef")
#
# print(ret.group())

#{m,}  匹配前一个字符至少出现m次
#{m,n}匹配前一个字符出现m次到n次

#匹配邮箱地址
# ret = re.match("[\w]{4,20}@163\.com$","liubin@163.com")
#
# print(ret.group())

#^ 匹配开头
#$  匹配结尾
#\b 匹配一个单词的边界
#\B 匹配非单词边界


# ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
# print(ret.group())


# ret = re.match("([^-]*)-(\d+)","010-12345678")
#
# print(ret.group())

# ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htASWml>")
#
# print(ret.group())
#解决方式
ret2 = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
print(ret2.group())


#search

retq = re.search(r"\d+", "阅读次数为 9999")

print(retq.group())#9999

ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret)
ret2 = re.sub(r"\d+", '2',"python = 3")

print(ret2)