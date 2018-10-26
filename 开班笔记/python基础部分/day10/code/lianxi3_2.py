s = input('')
d = {}
for y in s:
    if y not in d:
        d[y] = 1
    else:
        d[y] += 1
print(d)
