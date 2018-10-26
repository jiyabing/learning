#匹配文件中所有大写开头的单词
import re



pattern = r'\b[A-Z][a-z]*\b|\b[A-Z]+\b'

with open('abc.txt') as f:
	data = f.read()

l = re.findall(pattern, data)

print(l)