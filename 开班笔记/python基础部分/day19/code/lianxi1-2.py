class Student:
     def __init__(self,n,a,s):
          self.name = n
          self.age = a
          self.score =s

         
def input_student():
     lst = []
     while True:
          n = input('请输入姓名：')
          if not n:
               break
          a = int(input('请输入年龄：'))
          s = int(input('请输入成绩：'))
          stu = Student(n,a,s)
          lst.append(stu)
     return lst



def output_student(lst):
    for stu in lst:
        print('姓名：',stu.name,
              '年龄：',stu.age,
              '成绩：',stu.score)


def main():
    l = input_student()
    output_student(l)


main()
