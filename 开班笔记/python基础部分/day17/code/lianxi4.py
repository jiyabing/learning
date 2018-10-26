def fun():
    l = []
    while True:
        s = input('请输入：')
        if not s:
            break
        l.append(s)

    for i in enumerate(l,1):
        print('第%d行：%s' %i)

fun()
        
