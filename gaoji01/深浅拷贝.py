
a = [11,22,33]

b = a

print(id(a))
print(id(b))
#a和b指向同一存储空间
#💰浅拷贝


#深拷贝

import copy

c = copy.deepcopy(a)

#地址不一样了

print(id(a))
print(id(c))

