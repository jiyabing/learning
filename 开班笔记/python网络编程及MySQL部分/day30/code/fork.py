# coding:gbk
#osΪϵͳ���ģ�飬��ͬ����ϵͳʹ�������ͬ

import os
print('׼����������')
a = 1 #���д˳����,�ӽ�����Ҳ���б���a

pid = os.fork()

if pid < 0:
    print('��������ʧ��')
elif pid == 0:
    print('������һ���µĽ���a=',a)
else:
    print('����ԭ�еĽ���')

