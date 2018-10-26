docs = []

class Student():
	def __init__(self,n,a,s):
		self.name = n
		self.age = a
		self.score = s
	
	def get_info(self):
		return (self.name,self.age,self.score)
	
	def get_age(self):
		return self.age
	
	def get_score(self):
		return self.score
	
	def write_to_file(self,f):
		f.write(self.__name)
		f.write(',')
		f.write(str(self.__age))
		f.write(',')
		f.write(str(self.__score))
		f.write('\n')

		
#输入学生信息
def input_student():
	lst = []
	while True:
		name = input('请输入学生姓名：')
		if not name:
			return lst
		while True:
			try:
				age = int(input('请输入学生年龄：'))	
			except:
				print('请输入数字')
				continue
			else:
				break
		while True:
			try:
				score = int(input('请输入学生成绩：'))
			except:
				print('请输入数字')
				continue
			else:
				break
		#d = dict(name=name,age=age,score=score)
		stu = Student(name,age,score)
		#lst.append(d)
		lst.append(stu)

#打印学生信息
def output_student(lst):
	def biankuang():
		print('+'+'-'*14+'+'+('-'*7+'+')*2)
	
	def info(stu):
		print('|'+str(stu.name).center(14)+'|'+str(stu.age).center(7)+
		       '|'+str(stu.score).center(7)+'|')
	
	biankuang()
	print('|'+'name'.center(14)+'|'+'age'.center(7)+'|'+'score'.center(7)+'|')
	biankuang()
	for stu in lst:
		info(stu)
	biankuang()


#添加学生
def add_student():
	global docs
	docs += input_student()

#显示学生信息
def show_student():
	output_student(docs)


#删除学生函数
def del_student():
    name = input('输入要删除的学生姓名：')
    for stu in docs:
        if name == stu.name:
            docs.remove(stu)
            print('删除成功')
            return
    else:
        print('%s学生不存在' %name)

#修改学生函数
def xg_student():
    name = input('输入要修改的学生姓名：')
    for stu in docs:
        if name == stu.name:
            n = input('姓名：')
            a = int(input('年龄：'))
            s = int(input('成绩：'))
            stu.name = n
            stu.age = a
            stu.score = s
            print('修改成功')
            return
    else:
        print('%s学生不存在' %name)

#按成绩高低排序
def sort_score1():
	l = sorted(docs,key=lambda stu:stu.get_score(),reverse=True)
	output_student(l)

#按成绩低高排序
def sort_score2():
	l = sorted(docs,key=lambda stu:stu.get_score())
	output_student(l)

#按年龄高低排序
def sort_age1():
	l = sorted(docs,key=lambda stu:stu.get_age(),reverse=True)
	output_student(l)

#按年龄低高排序
def sort_age2():
	l = sorted(docs,key=lambda stu:stu.get_age())
	output_student(l)

#保存学生信息
def write_stu_info(lst):
	try:
		f = open('si.txt','w')
		for stu in lst:
			f.write('%s,%d,%d\n' %(stu.name,stu.age,stu.score))
		f.close()
	except IOError:
		print('保存失败！')
	else:
		print('保存成功！')

def save_info():
	write_stu_info(docs)

#导入学生信息
def import_stu_info():
	print('name'.center(14)+'age'.center(7)+'score'.center(7))
	lst = []
	try:
		f = open('si.txt')
		while True:
			s = f.readline()
			s = s.strip()
			if not s:
				f.close()
				break          
			l = s.split(',')
			print(l[0].center(14)+l[1].center(7)+l[2].center(7))
			d=dict(name=l[0],age=int(l[1]),score=int(l[2]))
			lst.append(d)
	except IOError:
		print('无任何学生信息,请先添加学生')
	else:
		print('导入成功！')
	return lst
