#添加学生函数
def input_student():
    lst = []#创建空列表存储学生信息（字典）
    while True:
        name = input('请输入学生姓名：')
        if name == '':
        #if not name:
            return lst
        age = int(input('请输入学生年龄：'))
        score = int(input('请输入学生成绩：'))
        d = dict(name=name,age=age,score=score)
        lst.append(d)
#l=input_student()
#print(l)

#学生输出函数
def output_student(lst):
    def info(d):
        print('|'+str(d['name']).center(14)+'|'+str(d['age']).center(7)+
              '|'+str(d['score']).center(7)+'|')
    def biankuang():
        print('+'+'-'*14+'+'+('-'*7+'+')*2)

    biankuang()
    print('|'+'name'.center(14)+'|'+'age'.center(7)+'|'+'score'.center(7)+'|')
    biankuang()
    for i in range(len(lst)):
        info(lst[i])
    biankuang()

#删除学生函数
def del_student(lst):
    name = input('输入要删除的学生姓名：')
    for d in lst:
        if name in d['name']:
            lst.remove(d)
            print('删除成功')
            return
    else:
        print('%s学生不存在' %name)

#修改学生函数
def xg_student(lst):
    name = input('输入要修改的学生姓名：')
    for d in lst:
        if name in d['name']:
            n = input('姓名：')
            a = int(input('年龄：'))
            s = int(input('成绩：'))
            d['name'] = n
            d['age'] = a
            d['score'] = s
            print('修改成功')
            return
    else:
        print('%s学生不存在' %name)

'''
def sort(lst,key):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j][key] > lst[j+1][key]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst
'''
#按年龄排序
def sort_age(d):
    return d['age']

#按成绩排序
def sort_score(d):
    return d['score']

'''
#按成绩高—低排序
def score1_student_sort(lst):    
    l = sort(lst,'score')[::-1]
    output_student(l)

#按成绩低—高排序
def score2_student_sort(lst):
    l=sort(lst,'score')
    output_student(l)
    
#按年龄高—低排序
def age1_student_sort(lst):
    l = sort(lst,'age')[::-1]
    output_student(l)

#按年龄低—高排序
def age2_student_sort(lst):
    l=sort(lst,'age')
    output_student(l)
'''
            
#output_student(l)
def show_menu():
    print('********************************')
    print('| 1)添加学生信息               |')
    print('| 2)显示所有学生的信息         |')
    print('| 3)删除学生信息               |')
    print('| 4)修改学生成绩               |')
    print('| 5)按学生成绩高-低显示学生信息|')
    print('| 6)按学生成绩低-高显示学生信息|')
    print('| 7)按学生年龄高-低显示学生信息|')
    print('| 8)按学生年龄低-高显示学生信息|')
    print('| 9)保存学生信息               |')
    print('|10)读取学生信息               |')
    print('| q)退出                       |')
    print('********************************')

def main():
    import time
    docs=[]     #此列表存储学生信息
    while True:
        show_menu()
        s=input('请选择：')

        #根据用户做出的选择处理相应的事情
        if s == 'q':
            return
        elif s == '1':
            docs += input_student()
            time.sleep(1.5)
        elif s == '2':
            output_student(docs)
            time.sleep(1.5)
        elif s == '3':
            del_student(docs)
            time.sleep(1.5)
        elif s == '4':
            xg_student(docs)
            time.sleep(1.5)
        elif s == '5':
            #score1_student_sort(docs)

            l = sorted(docs,key=sort_score,reverse=True)
            output_student(l)

            time.sleep(1.5)
        elif s == '6':
            #score2_student_sort(docs)

            l = sorted(docs,key=sort_score)
            output_student(l)

            time.sleep(1.5)
        elif s == '7':
            #age1_student_sort(docs)

            l = sorted(docs,key=sort_age,reverse=True)
            output_student(l)

            time.sleep(1.5)
        elif s == '8':
            #age2_student_sort(docs)

            l = sorted(docs,key=sort_age)
            output_student(l)

            time.sleep(1.5)
        
main()
    
