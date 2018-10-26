#此示例示意星号元组形参
def func(*args):
    print('实参个数是：',len(args))
    print('args的值是：',args)

func(1,2,3)
func('a',True,2,3.3,None)
