d = {'0':'周日','日':'周日','1':'周一','一':'周一','2':'周二','二':'周二',
     '3':'周三','三':'周三','4':'周四','四':'周四','5':'周五','五':'周五',
     '6':'周六','六':'周六'}

s = input('输入任意值：')
print(d.get(s,'字典内没有相应的数据'))
