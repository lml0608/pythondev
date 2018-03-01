# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


old_filename = input('输入要拷贝的文件名：')


oldfile = open(old_filename,'r')

if oldfile:


    #提取文件后缀：如.txt
    fileFlagNum = old_filename.rfind('.')

    if fileFlagNum > 0:

        fileFlag = old_filename[fileFlagNum:]


    #新文件名字

    newFileName = old_filename[:fileFlagNum] + '[复件]' +fileFlag


    newfile = open(newFileName,'w')


    for lineContent in oldfile.readlines():
        newfile.write(lineContent)



    oldfile.close()

    newfile.close()




