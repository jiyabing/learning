import os
import shutil
import getpass

# 源目录,这里假设是桌面需要程序自动整理的路径
dirpath = "C:\\Users\\%s\\Desktop" % getpass.getuser()
# 根路径，存放归档数据
rootpath = dirpath + "\\文件整理\\"

# 各类office相关文件存档地址
office = rootpath + "office文件\\"
# pic相关文件存档地址
pic = rootpath + "图片\\"
# txt相关文件存档地址
txt = rootpath + "文本文件\\"
# 各种文件夹相关文件存档地址
dirss = rootpath + "各种文件夹\\"
# tar相关文件存档地址
tar = rootpath + "压缩包\\"
# 音乐相关文件存档地址
mp3 = rootpath + "音乐\\"
# 视频相关文件存档地址
video = rootpath + "视频\\"
# 无分类文件
unknowFile = rootpath + "未分类文件\\"


def filemanage(dp):
    # 转成元组表示
    tt = tuple(os.walk(dp))
    # print(len(tt[0][1]))
    # 一级目录下的所有文件夹
    dirs = tt[0][1]
    # 一级目录下的所有文件
    files = tt[0][2]
    print("文件夹总数量: ", len(dirs), "文件总数据量: ", len(files), "总共文件数:", len(dirs) + len(files))
    print("====================移动文件开始==================================")
    for var in tt[0][2]:
        filename = dp + "\\" + var
        # print(filename)
        if filename.endswith("excel") or filename.endswith("pdf") or filename.endswith("doc") \
                or filename.endswith("docx") or filename.endswith("ppt") or filename.endswith("pptx") \
                or filename.endswith("xls") or filename.endswith("xlsx"):
            if not os.path.exists(office):
                os.makedirs(office)
                print(office, "文件夹不存在，已生成!")
            shutil.move(filename, office)
        elif filename.endswith("jpg") or filename.endswith("gif") or filename.endswith("png"):
            if not os.path.exists(pic):
                os.makedirs(pic)
                print(pic, "文件夹不存在，已生成!")
            shutil.move(filename, pic)
        elif filename.endswith("txt"):
            if not os.path.exists(txt):
                os.makedirs(txt)
                print(txt, "文件夹不存在，已生成!")
            shutil.move(filename, txt)
        elif filename.endswith("gz") or filename.endswith("zip") or filename.endswith("rar"):
            if not os.path.exists(tar):
                os.makedirs(tar)
                print(tar, "文件夹不存在，已生成!")
            shutil.move(filename, tar)
        elif filename.endswith("mp3"):
            if not os.path.exists(mp3):
                os.makedirs(mp3)
                print(mp3, "文件夹不存在，已生成!")
            shutil.move(filename, mp3)
        elif filename.endswith("avi") or filename.endswith("mp4") or filename.endswith("wam"):
            if not os.path.exists(video):
                os.makedirs(video)
                print(video, "文件夹不存在，已生成!")
            shutil.move(filename, video)
        else:
            if not (filename.endswith('.lnk') or filename.startswith('文件整理')):
                if not os.path.exists(unknowFile):
                    os.makedirs(unknowFile)
                    print(unknowFile, "文件夹不存在，已生成!")
                shutil.move(filename, unknowFile)
                print("无分类的文件: " + filename)
    print("====================文件整理完毕==================================")
    print("====================移动目录开始==================================")
    for var in tt[0][1]:
        tempdir = dp + "\\" + var
        if var != '文件整理':
            shutil.move(tempdir, dirss + "\\" + var)
            print("移动" + tempdir + "到" + dirss + "路径完毕.......")
    print("====================文件夹整理完毕================================")
    


def do_file(): # 开始分类
    try:
        filemanage(dirpath)
    except PermissionError:
        print('部分文件没有权限,可能是正在运行')
    except Exception as e:
        print(e)

if __name__ == '__main__':
	do_file()
