from menu import show_menu
import caozuo as cz

def main():
    #docs = []    #此列表存储学生信息
    while True:
        show_menu()
        s=input('请选择：')

        #根据用户做出的选择处理相应的事情
        if s == 'q':
            return
        elif s == '1':
            cz.add_student()

        elif s == '2':
            cz.show_student()

        elif s == '3':
            cz.del_student()

        elif s == '4':
            cz.xg_student()

        elif s == '5':
            cz.sort_score1()

        elif s == '6':
            cz.sort_score2()

        elif s == '7':
            cz.sort_age1()

        elif s == '8':
            cz.sort_age2()

        elif s == '9':
            cz.save_info()

        elif s == '10':
            cz.import_stu_info()


main()
