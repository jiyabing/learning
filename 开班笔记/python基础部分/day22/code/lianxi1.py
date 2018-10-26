def cp(filename1,filename2):
    try:
        with open(filename1,'rb') as fr:
            with open(filename2,'wb') as fw:
                while True:
                    b = fr.read(4096) #防止文件过大
                    if not b:
                        break
                    fw.write(b)
    except:
        return
    else:
        return True

def main():
    filename1 = input('输入源文件：')
    filename2 = input('输入目标文件:')
    if cp(filename1,filename2):
        print('复制成功')
    else:
        print('复制失败')

main()
