import re

obj = re.compile(r'(?P<dog>ab)(cd)(?P<pig>ef)')

print('flags:',obj.flags)  #标志位常量
print('pattern:',obj.pattern) #正则表达式
print('groupindex:',obj.groupindex) #捕获组字典
print('groups:',obj.groups)  #子组数量
print('======================')

match_obj = obj.search('abcdefghi')
print(match_obj.pos)  #目标字符串开头位置
print(match_obj.endpos)  #目标字符串结束位置
print(match_obj.re)  #正则表达式对象
print(match_obj.string)  #目标字符串
print(match_obj.lastgroup) #最后一组的组名
print(match_obj.lastindex) #最后一组是第几组
print('==========================')

print(match_obj.start()) #匹配到内容的开始位置
print(match_obj.end())  #匹配到内容的结束位置
print(match_obj.span())   #匹配到内容的起止位置
print('====================================')

print(match_obj.group()) #匹配正则表达式整体内容
print(match_obj.group(1)) #匹配某个子组内容
print('============================================')

print(match_obj.groups())
print(match_obj.groupdict())