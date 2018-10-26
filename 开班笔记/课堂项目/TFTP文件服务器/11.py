#!/usr/bin/python
import sys
print('该脚本名字叫：',sys.argv[0])
if len(sys.argv) != 3:
	sys.exit()
else:
	print({'name':sys.argv[1],'age':int(sys.argv[-1])})
