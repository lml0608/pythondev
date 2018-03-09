

'''
进程间通信

先进先出FIFO 队列Queue

后进先出，队列


'''


from multiprocessing import Queue

#初始化对象，最多可接收三条Put消息


q = Queue(3)


q.put("消息1")
q.put("消息2")
print(q.full()) #Flase
q.put("消息3")
print(q.full()) #True
#print(q.qsize())

print(q.get())
print(q.get())
#print(q.qsize())


#print(q.empty())

q.put("hha")
print(q.empty())

q.get_nowait()