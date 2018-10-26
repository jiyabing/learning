v = 100    #全局变量
def fun1():
    v = 200
    print('fun1里的v的值是：',v)

    #定义另一个函数 fun2,然后调用
    def fun2():
        print('fun2里的v=',v)

    fun2()

fun1()
print('全局的v=',v)
