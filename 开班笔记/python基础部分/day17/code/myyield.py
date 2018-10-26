def myyield():
    print('即将生成2')
    yield 2
    print('即将生成3')
    yield 2 + 1
    print('即将生成5')
    yield 5
    print('即将生成7')
    yield 7
    print('生成器函数调用结束')

gen = myyield() #gen绑定生成器对象，此对象为可迭代对象
print(gen) 
it = iter(gen)
print(next(it))
print('---------')
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    print(x)
