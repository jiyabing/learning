'''
print('第一题')
l = []
def input_number():
    while True:
        i = int(input('输入数字（-1结束）：'))
        if i < 0:
            break
        l.append(i)
    return l

input_number()
print('刚才输入的整数是：',l)
'''



print('第二题')
def isprime(x):
    if x <= 1:  #排除小于2的情况
        return False
    if x == 2:
        return True
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

if isprime(9):
    print('素数')
else:
    print('不是素数')


print('第三题')
def prime_m2n(m,n):
    l = []
    for i in range(m,n):
        if isprime(i):
            l.append(i)
    return l

    #return list(filter(isprime,range(m,n)))

print(prime_m2n(10,20))


print('第四题')
def primes(n):
    l = []
    for i in range(n):
        if isprime(i):
            l.append(i)
    return l

    #return prime_m2n(2,n)

print(primes(10))

                
        
