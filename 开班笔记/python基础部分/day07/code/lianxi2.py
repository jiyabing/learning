#打印'AaBbCcDd.....YyZz'
for i in range(ord('A'),ord('Z')+1):
    print(chr(i)+chr(i).lower(),end='')
print()


n = int(input('输入整数：'))
for i in range(1,n+1):
    for j in range(i,i+n):
        print('%2d' %j,end=' ')
    print()
