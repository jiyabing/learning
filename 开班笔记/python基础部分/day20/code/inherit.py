class Human:
    def say(self,what):
        print('说:',what)
    def walk(self,distance):
        print('走了',distance,'公里')


class Student(Human):
    def study(self,subject):
        print('正在学习:',subject)


class Teacher(Student):
    def teach(self,subject):
        print('老师正在教:',subject)

h1 = Human()
h1.say('今年天气不错！')
h1.walk(5)

s1 = Student()
s1.say('今天晚上吃什么？')
s1.walk(10)
s1.study('Python')

t1 = Teacher()
t1.say('好好学习')
t1.walk(1)
t1.teach('数学')
t1.study('做菜')
