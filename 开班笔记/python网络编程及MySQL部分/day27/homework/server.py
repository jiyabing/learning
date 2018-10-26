from socket import *

sockfd = socket(AF_INET,SOCK_STREAM,0)

sockfd.bind(('176.215.155.131',9999))

sockfd.listen(10)

while True:
    print('等待连接')
    conn,addr = sockfd.accept()
    print(addr,'已连接')

    while True:
        data = conn.recv(1024)
        print(data.decode('gbk'))
        if not data:
            print('对方已断开')
            break

        msg = input('输入内容:')
        conn.send(msg.encode('gbk'))
        if not msg:
            break

    conn.close()

sockfd.close()
