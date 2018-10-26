l = []
while True:
    n = input('输入正整数：')
    if n == '' or int(n) < 0:
        break
    l.append(int(n))

#print(l)
print('和是：',sum(l))
l2 = sorted(l)
#print(l)
#print(l2)
print('最大数是：',l2[-1])
print('第二大数是：',l2[-2])
l.remove(min(l))
print(l)

