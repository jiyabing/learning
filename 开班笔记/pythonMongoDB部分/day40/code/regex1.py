import re


pattern = r'\d+'
#匹配内容返回迭代器
it = re.finditer(pattern,'2008年是个多事之秋，512地震，0808奥运会')
print(it)
for i in it:
	print(i.group())
	

#match匹配
obj = re.match('foo','foo,food on the desk')
print(obj.group())

try:
	obj = re.fullmatch('\w+','adfdc#a233')
	print(obj.group())
except AttributeError as e:
	print(e)