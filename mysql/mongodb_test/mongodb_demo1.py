
from pymongo import *


#建立连接
client = MongoClient('mongodb://39.108.138.21:27017')

print(client)
#切换数据库
db = client.test


print(db)

#获取集合

stu = db.stu

stu.insert({'name':'张三封'})