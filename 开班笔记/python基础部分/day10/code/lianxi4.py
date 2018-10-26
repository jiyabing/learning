
print('第一题')
sum = 1
for i in range(9):
    sum = (sum+1) * 2
print(sum)

'''
def func(n):
    if n == 1:
        return 1
    return (func(n-1)+1) * 2

print(func(100))
'''

'''
print('第二题')
#方法一
for i in range(10000):
    sum = 1
    for j in range(2,i):
       if i % j ==0:
           sum += j
    if i == sum:
        print(i)
'''

#方法二
n = 1
c = 0
while True:
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    if n == sum:
        print(n)
        c += 1
    n += 1
    if c == 4:
        break



'''
print('第三题')
n = int(input('输入整数：'))
l = []  #第四题要用
for i in range(1,n+1):
    #print(' '*(n-i),end='')
    s = ''
    for j in range(1,i+1):
        s += str(j)
        #print(j,end='')
    for k in range(i-1,0,-1):
        s += str(k)
        #print(k,end='')
    l.append(s)  #第四题要用
    #print()
    print(s.center(2*n-1))
#print(l)

#第四题
for i in reversed(l):
    if i != l[-1]:
        print(i.center(2*n-1))
'''
