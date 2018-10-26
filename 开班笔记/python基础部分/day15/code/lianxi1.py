import time,sys


while True:
    #print('\r %2d:%2d:%2d' %time.localtime()[3:6],end='')
    print('\r%02d:%02d:%02d' %time.localtime()[3:6],end='')
    #在cmd内可以看出效果，在IDLE内无法看出效果
    time.sleep(1)



'''
y=int(input('年：'))
m=int(input('月：'))
d=int(input('日：'))
t=time.mktime((y,m,d,0,0,0,0,0,0))
print(t)
time_tuple = time.localtime((t))
week = time_tuple[6]
    
l=[1,2,3,4,5,6,7]
print(l[week])


t= time.time()-t
day=t//(60*60*24)
print(day)
'''
