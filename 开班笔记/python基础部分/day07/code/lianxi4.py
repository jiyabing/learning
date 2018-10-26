L = []
while True:
    s = input('输入字符串：') 
    if s == '':
        break
    else:
        L += [s]
print(L)
print(L[::-1])#反向输出
