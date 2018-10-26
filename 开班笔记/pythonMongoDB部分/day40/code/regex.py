import re

pattern = r'\s+'

#获取正则表达式对象
obj = re.compile(pattern)
#l = obj.findall('abcddfadfad',6,9)

#l1 = re.findall(pattern, 'abcddfadfad')
#print(l)
#print(l1)

#匹配目标字符串进行切割
l = obj.split('hello world  	hello kitty nihao china')
print(l)


#替换目标字符串中匹配到的内容
s = obj.sub('##','hello world  	hello kitty nihao china',3)
print(s)

s1 = obj.subn('##','hello world  	hello kitty nihao china')
print(s1)
