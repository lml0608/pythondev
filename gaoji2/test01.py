
import pdb
def fib(times):


    n = 0

    a,b = 0,1

    while n < times:

        #print(b)

        yield b
        a,b= b,a+b


        n += 1
    return "done"

x =fib(5)

print(x)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
#print(next(x))

