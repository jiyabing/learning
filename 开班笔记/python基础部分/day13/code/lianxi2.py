print('第一题')
def myfac(x):
    if x == 1:
        return 1
    return x * myfac(x-1)

print(myfac(4))

print('第二题')
def sum_jc(m,n):
    return sum(map(myfac,range(m,n+1)))

print(sum_jc(1,4))


print('第三题第一问')
l = [[3,5,8],10,[[13,14],15],18]
def print_list(lst):
    for i in lst:
        if type(i) == int:
            print(i)
        elif type(i) == list:
            print_list(i)

print_list(l)

print('第四题第二问')
def sum_list(lst):
    s = 0
    for i in lst:
        if type(i) is list:
            s += sum_list(i)
        else:
            s += i
    return s

print(sum_list(l))

