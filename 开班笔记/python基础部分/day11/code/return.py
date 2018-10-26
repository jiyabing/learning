#此示例示意return语句的用法
def hello():
    print('hello aaa')
    print('hello bbb')
    return [1,23]   #用于返回到调用的地方
    print('hello ccc')

v = hello()
print(v)
