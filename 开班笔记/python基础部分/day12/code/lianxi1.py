print('第一题')
def mysum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

print(mysum(100))

print('第二题')
#方法一
def mysum1(start ,stop = 0,step = 1):
    sum = 0
    if stop == 0:
        start,stop = stop,start
    for i in range(start ,stop ,step):
        sum += i
    return sum

#方法二
def mysum2(*args):
    sum = 0
    for i in range(*args):
        sum += i
    return sum

print(mysum1(100))
print(mysum2(2,5))
print(mysum2(1,10,2))
