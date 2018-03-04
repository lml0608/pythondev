


'''

_x 单前置下划线，私有属性或方法，禁止导入，类和子类可以访问

__xx双前置下划线，避免与子类中属性起冲突，无法在外部直接访问

xx_ 单后置下划线，避免与关键词冲突
'''
class Test(object):


    def __int__(self):

        self.__num = 100

    def setNum(self,newnum):

        self.__num = newnum

    def getNum(self):

        return self.__num

t = Test()


print(t.getNum())
t.setNum(50)

print(t.getNum())




