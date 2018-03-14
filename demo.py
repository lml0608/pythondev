# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


import csv

a = 16598475

lista = []
for i in range(1,2500):

    a += 1

    lista.append(a)

with open('cusid.csv','w',newline='') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel',delimiter='\n')
    spamwriter.writerow(lista)




