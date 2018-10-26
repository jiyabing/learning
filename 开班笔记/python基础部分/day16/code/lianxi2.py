print('第一题')
def fn(n):
    H = 100
    sum = 100
    for i in range(n):
        H /= 2
        sum += H*2
    return (H,sum-H)

#递归算反弹高度
def func(h,n):
    if n == 1:
        return h/2
    return func(n-1)/2

print(fn(10))



'''
print('第二题')
for i in range(1,10):
    for j in range(1,i+1):
        print('%dx%d=%-2d  ' %(j,i,j*i),end='')
    print()


print('第三题')
def func(n):
    if n <= 2:
        return print(n)
    print('%d=' %n,end='')
    for i in range(2,n):
        while n != i:
            if n%i != 0:
                break
            print('%d*' %i,end='')
            n = n/i            
    print(int(n))

func(100)
'''               
        
