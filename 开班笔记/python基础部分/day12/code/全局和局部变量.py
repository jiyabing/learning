a = 1
b = 2
def fn(c):
    d = 4
    #print(a,b,c,d) #有错，此时a变量还不存在
    a = 5
    print(a,b,c,d)

fn(3)
print('a=',a)
print('b=',b)
