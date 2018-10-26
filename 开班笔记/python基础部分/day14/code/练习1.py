from math import factorial as fac 
def fun(n):
    #Sn=0
    #for i in range(n):
        #Sn += 1/fac(i)

    Sn=sum(map(lambda x:1/fac(x),range(n)))

    return Sn

print(fun(10))



def fun1(x,n):
    s = 0
    for i in range(n):
        s += pow(x,i)/fac(i)

    #s=sum(map(lambda i:x**i/fac(i),range(n)))
    
    return s



print(fun1(3.1,10))
