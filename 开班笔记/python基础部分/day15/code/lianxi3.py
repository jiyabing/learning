'''
print('第一题')
def ring(h,m):
    import time,sys
    while True:
        l = time.localtime()
        if h == l[3] and m == l[4]:
            print('时间到...')
            time.sleep(5)
            sys.exit()
        print('%d:%d:%d' %l[3:6])
        time.sleep(1)

ring(17,40)
'''

print('第二题')
def ddz():
    import random
    s_jc = {i+j for i in '\u2660\u2663\u2665\u2666'
            for j in ['A','2','3','4','5','6','7','8','9','10',
                        'J','Q','K']}
    s_jc.add('大王')
    s_jc.add('小王')

    def fp():
        nonlocal s_jc
        p=random.sample(s_jc,17)
        s_jc = s_jc - set(p)
        p.sort()
        return p

    s = input('按<回车>发牌')
    c = 1
    while not s:
        print('第%d个人的牌是：%r' %(c,fp()))
        c += 1
        if c == 4:
            break
    print('底牌是：',list(s_jc))
    
    '''
    s1 = []
    
    for i in range(17):
        d = random.choice(s_jc)
        s1.append(d)
        s_jc.remove(d)

    s2 = []
    for i in range(17):
        d = random.choice(s_jc)
        s2.append(d)
        s_jc.remove(d)

    s3 = []
    for i in range(17):
        d = random.choice(s_jc)
        s3.append(d)
        s_jc.remove(d)
    '''
    '''
    p1=input('按<回车>发牌')
    if not p1:
        print('第一个人的牌：',fp())

    p2=input()
    if not p2:
        print('第二个人的牌：',fp())
    p3=input()
    if not p3:
        print('第一个人的牌：',fp())
    p4=input()
    if not p4:
        print('底牌是：',s_jc)
    '''   
    

ddz()
     

