#���������ӽ���

import os

#����һ���ӽ���
pid1 = os.fork()

if pid1 < 0:
    print('����һ���ӽ���ʧ��')

elif pid1 == 0:
    #���������ӽ���
    pid2 = os.fork()
    if pid2 < 0:
        print('���������ӽ���ʧ��')
    elif pid2 == 0:
        print('����һ����')
    else:
        #һ���ӽ����˳���ʹ�����ӽ��̳�Ϊ�¶�
        os._exit(0)

else:
    #�ȴ�һ���ӽ����˳�
    os.wait()
    print('�������̸�����')