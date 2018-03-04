
def test(num):

    print("---1----")

    def test_in():
        print("---2----")

        print(num + 100)

    print("---3----")

    return  test_in

test(200)()

# x = test(100)
#
# print(type(x))  #<class 'function'>
#
# x()