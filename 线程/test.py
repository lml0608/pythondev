def delspace(filename):
    func = lambda text: text.strip()
    with open(filename, 'r+') as f:
        ls = map(func, f)



        print(ls)

        f.seek(0)

        with open("new.txt",'w') as nf:
            nf.write(''.join(ls))
        #f.write(''.join(ls))


if __name__ == '__main__':
    delspace('wx.txt')