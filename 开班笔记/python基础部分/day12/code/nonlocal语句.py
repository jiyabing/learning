v = 100
def outter():
    v = 200
    print('outter里的v=',v)

    def outter1():
        global v    #调用全局的v
        #nonlocal v #此时调用outter内的v
        v = v + 3
        print('outter1里的v=',v)

    outter1()
    print('调用outter1后，outter里的v=',v)

outter()
print('全局里的v的值：',v)
