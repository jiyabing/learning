s = 'abcde'
for x in s:
    print('---->',x)
    if x == 'c':
        break
else:
    print('for循环语句因迭代的结束而终止')
