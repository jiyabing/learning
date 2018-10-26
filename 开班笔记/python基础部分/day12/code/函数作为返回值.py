def get_op():
    s=input('请输入您的操作：')
    if s == '求最大':
        return max
    elif s == '求最小':
        return min
    elif s == '求和':
        return sum

L = [2,3,4,5]
print(L)
f = get_op()
print(f(L))
