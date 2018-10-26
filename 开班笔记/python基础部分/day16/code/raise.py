def make_except(n):
    #假设n必须是0-100之间的数
    print('begin..')
    if n > 100:
        raise ValueError
    if n < 0:
        raise ValueError('参数小于零错误:%d' %n)
    print('end')


n = int(input('输入整数'))
try:
    make_except(n)
except ValueError as e:
    print('make_except抛出了异常，此异常状态以处理')
    print('错误的值：',e)
    print('发生错误')
print('程序正常完成')
