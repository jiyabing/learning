def myodd(k,j):
    while k < j:
        if k%2 == 1:
            yield k
        k += 1

l=[x for x in myodd(1,10)]
print(l)

for i in myodd(10,20):
    print(i)


