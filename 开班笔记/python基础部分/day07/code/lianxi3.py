sum = 0
for i in range(1,100):
    if i%5 == 0 or i%7 == 0 or i%11 == 0:
        continue
    sum += i
    print(i)
print(sum)
