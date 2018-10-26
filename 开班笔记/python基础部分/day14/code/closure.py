#1.fn为内嵌函数
#2.fn 用到了fn外部的变量
#3.make_power将fn绑定的函数对象返回给调用者

def make_power(y):
    def fn(x):
        return x ** y
    return fn

pow2=make_power(2)
print('5的平方是：',pow2(5))
