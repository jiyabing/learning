
#打印三角形
print('第一题')
n = int(input('输入整数：'))
for i in range(1,n+1):
    print('*'*i)

for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)

for i in range(n,0,-1):
    print(' '*(n-i)+'*'*i)

for i in range(n,0,-1):
    print('*'*i)



'''
#2.输入一个unicode的开始值，用变量begin绑定
#  输入一个unicode的结束值，用变量end绑定
#  打印开始值至结束值所对应的文字，生成字符串并打印
print('第二题')
begin = int(input('请输入unicode开始值：'))
end = int(input('请输入unicode结束值：'))
for i in range(begin,end):
    print(chr(i),end='')
'''

'''
#3.输入一个整数（代表树干的高度）
#  打印圣诞树
print('第三题')
n = int(input('输入一个整数：'))
for i in range(1,n+1):
    print(' '*(n-i) + '*'*(2*i-1))
    #print('*'*(2*i-1).center(2*n-1))
for i in range(n):
    print('%*s' %(n,'*'))
'''

'''
#4.输入一个整数（代表树干的高度）
#  打印圣诞树
print('第四题')
n = int(input('输入一个整数：'))
for i in range(1,n+1):
    print(' '*(n-i)+str(i)*(2*i-1))
for i in range(n):
    print(' '*(n-1)+'*')
'''


'''
#输入一个正整数，打印这个数是否是素数
#只能被1和自身整除的整数，1除外
print('第五题')
n = int(input('输入一个正整数：'))
for i in range(2,n):
    if n%i == 0:
        print('不是素数')
        break
else:
    print('素数')
'''
    
