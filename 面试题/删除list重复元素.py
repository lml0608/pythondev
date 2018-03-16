
#方法一是用set

a = [1,2,4,2,4,5,6,5,8,9,0]
print(set(a))

#方法二

b = {}

b = b.fromkeys(a)

#c = list()
print(b)

print(b.keys())

c = list(b.keys())

print(c)