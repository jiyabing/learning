import os,sys


#��������
os._exit(0)


try:
    sys.exit(1):
except SystemExit as e:
    print(e)

#��ӡ���̽�����
sys.exit('�����ѽ���')

print('Game over')