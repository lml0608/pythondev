class Test(object):


    def __int__(self):

        self.__num = 100

    def setNum(self,newnum):

        self.__num = newnum

    def getNum(self):

        return self.__num

t = Test()



t.setNum(50)

print(t.getNum())
t.setNum(500)
print(t.getNum())