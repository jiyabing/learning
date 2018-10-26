#continue_for
#打印5以内除了2的整数
for i in range(5):
    if i == 2:
        continue
    print(i)


#continue_while
#打印偶数
i = 0
while i <= 10:
    if i%2 == 1:
        i += 1
        continue
    else:
        print(i)
    i += 1
