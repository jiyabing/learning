l = []
while True:
    n = int(input('Number:'))
    if n == -1:
        break
    l.append(n)
print(l)
print(sum(l))



l2 = []
for s in l:
    if s not in l2:
        l2.append(s)
print(l2)


l3 = []
for s in l:
    if l.count(s) == 2:
        if s not in l3:
            l3.append(s)
print(l3)
            
