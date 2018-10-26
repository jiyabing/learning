s = input('输入任意字符串：')
c = 0

'''
#方法一
for x in s:
    if x == ' ':
        c += 1
print('共有%d个空格' %c)
'''


#方法二
i = 0
while i < len(s):
    if s[i] == ' ':
        c += 1
    i += 1
print('共有%d个空格' %c)
