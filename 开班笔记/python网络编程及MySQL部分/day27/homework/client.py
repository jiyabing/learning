from socket import *
sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.connect(('176.215.155.131',9999))
print('连接成功')
while True:
    msg = input('输入内容>>')
    sockfd.send(msg.encode('gbk'))
    if not msg:
        break
    data = sockfd.recv(1024)
    print(data.decode('gbk'))
    if not data:
        print('对方已断开')
        break
sockfd.close()