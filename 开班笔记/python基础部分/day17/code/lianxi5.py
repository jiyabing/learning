
print('第一题')
def fib(n):
    if n <= 0:
        return
    a,b=1,1
    for _ in range(n):
        yield a
        a,b = b,a+b


for i in fib(20):
    print(i)

print(sum(fib(30)))


print('第二题')
def yhsj(n):
    l = [1]
    for _ in range(n):
        yield l
        #l = [sum(i) for i in zip([0]+l,l+[0])]
        l=list(map(lambda x,y:x+y,[0]+l,l+[0]))


def out_yhsj(n):
    for i in yhsj(n):
        s = ' '.join(map(str,i))
        print(s.center(2n-1))

out_yhsj(5)

