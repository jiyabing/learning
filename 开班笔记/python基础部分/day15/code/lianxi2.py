import random
l1=[chr(x) for x in range(65,91)]
l2=[chr(x) for x in range(97,103)]
l3=[x for x in range(1,10)]
s1=''.join(l1)
s2=''.join(l2)
s3=''.join(map(str,l3))
s=s1+s2+s3+'_'

sr=''
for i in range(6):
    sr += random.choice(s)
print(sr)


def get_passwd(n):
    '生成n位的随机密码'
    passwd = ''
    st='0123456789_'
    for i in range(ord('A'),(ord('Z')+1)):
        st += (chr(i)+chr(i).lower())
    for i in range(n):
        passwd += random.choice(st)
    return passwd

print('密码：',get_passwd(8))
        
