a = 1
b = 2
def fx(b,c):
    print(a,b,c)
    print('全局变量的字典是：',globals())
    print('局部变量的字典是：',locals())
    print('此处访问全局变量b的值：',globals()['b'])
    

fx(3,4)
