#print('第一题')
#n = int(input('输入一个正整数：'))
#i = 1
'''
while i <= n:
    print('*'*i)
    i +=1
'''

'''
while i <= n:
    print('%*s' %(n,'*'*i))
    i += 1
'''

'''
while n >= 1:
    print('*'*n)
    n -= 1
'''

'''
i = n
while n >= 1:
        print('%*s' %(i,'*'*n))
        n -= 1
'''

'''
print('第二题')
begin = int(input('输入开始数：'))
end = int(input('输入结束数：'))
i = 0
if begin >= end:
    while begin >= end:
        print('%-3d' %begin,end = ' ')
        i += 1
        if i%5 == 0:
            print()
        begin -= 1
else:
    while begin < end:
        print('%-3d' %begin,end = ' ')
        i += 1
        if i%5 == 0:
            print()
        begin += 1
'''

print('第三题')
i = ord('A')
j = ord('Z')
while i <= j:
    print(chr(i)+chr(i+32),end='')
    #print(chr(i)+chr(i).lower(),end='')
    i += 1


    


