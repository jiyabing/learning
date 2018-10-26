s={'gs','js','zg','ny'}
for x in s:
    print(x)

it = iter(s)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    print(x)
