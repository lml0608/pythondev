
'''

'''

from threading import Thread

import time

def test():

    print("---hhhh---")

    time.sleep(1)

for i in range(5):

    print(time.ctime())

    t = Thread(target=test)


    t.start()

    #time.sleep(5)
    print(time.ctime())