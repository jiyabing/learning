#death_loop.py
s = ''
while True:
    a = input('请输入文字（***结束）：')
    if a == '***':
        break
    s += a+'\n'
print('您刚才输入的是：')
print(s)
