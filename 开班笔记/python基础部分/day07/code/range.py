for x in range(4):
    print(x)

#c = 0
for i in range(3,8):
    print(i,end=' ')
    #c += 1
    if (i-8+1)%5 == 0:#当前值减开始值加1再整除5
        print()

j = 10
for j in range(1,j):
    print(j)#共打印了9行
    j -= 2
print('dfd',j)#此时的j等于7
    
