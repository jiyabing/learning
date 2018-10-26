print('第一题')
L = []
n = int(input('请输入一个正整数：'))
for i in range(1,n+1):
    if i < 2:
        continue
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        L.append(i)
print(L)
print('和为：',sum(L))


print('第二题')
lst = [i for i in range(100) if (i*(i+1)) % 11 == 8]
print(lst)

print('第三题')

#方法一
lib = []
a,b = 0,1
for i in range(20):
    lib.append(b)
    a,b = b,a+b
print(lib)


#方法二
l = [1,1]
while len(l) < 20:
    l.append(l[-1]+l[-2])
print(l)

    
