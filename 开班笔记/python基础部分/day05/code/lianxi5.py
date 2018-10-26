s1 = input('请输入第一行字符串：')
s2 = input('请输入第二行字符串：')
s3 = input('请输入第三行字符串：')
l = (max(len(s1),len(s2),len(s3)) + 2)
l1 = (l-len(s1))//2
l2 = (l-len(s2))//2
l3 = (l-len(s3))//2
print('+'+'-'*l+'+')
print('|'+' '*l1+s1+' '*((l-len(s1))-l1)+'|')
print('|'+' '*l2+s2+' '*((l-len(s2))-l2)+'|')
print('|'+' '*l3+s3+' '*((l-len(s3))-l3)+'|')
print('+'+'-'*l+'+')
