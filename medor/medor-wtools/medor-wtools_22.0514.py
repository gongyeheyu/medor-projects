# -*- coding: utf-8 -*-
import numbers
from os import system
import socket
import re, os 
import string
import random

def start():
    print ("0.退出")
    print ("1.应用程序")
    startcho = int(input("请输入数字来执行你的操作"))
    exit = startcho == 0
    gotoapps = startcho == 1
    if exit:
        print("感谢使用,再见")
    elif gotoapps:
        apps()
    else:
         input("输入错误")
         cls()
         start()

def apps():
    print('''
    1.IP地址
    2.软件查询
    3.本地连接
    4.清理垃圾
    5.写入文件
    6.Windows修复
    7.开始
    8.关于
    9.随机字符生成''')
    appscho = int(input("请输入"))
    int(appscho)
    if appscho == 1:
        IP地址()
    elif appscho == 2:
        软件查询()
    elif appscho == 3:
        #本地连接()
        网络信息()
    elif appscho == 4:
        清理垃圾()
    elif appscho == 5:
        写入文件()
    elif appscho == 6:
        Windows修复()
    elif appscho == 7:
        start()
    elif appscho == 8:
        关于()
    elif appscho == 9:
        随机字符生成()
    else :
        input("输入错误")
        cls()
        apps()

def IP地址():
    # 获取本机计算机名称
    hostname = socket.gethostname()
    # 获取本机ip
    ip = socket.gethostbyname(hostname)
    print("主机名" + hostname)
    print("IP地址" + ip)
    back()

def 软件查询():
    print("开发中...")
    back()   
    

#def 本地连接(): 
#   print("开发中...")
#220701 GONGYE Heyu

def 网络信息():
    print(os.system('netstat -sera'))
    print(os.system('ipconfig /all'))
#220701 GONGYE Heyu

def 清理垃圾():
    str 
    del_extension = {
    '.tmp': '临时文件',
    '._mp': '临时文件_mp',
    '.log': '日志文件',
    '.gid': '临时帮助文件',
    '.chk': '磁盘检查文件',
    '.old': '临时备份文件',
    '.xlk': 'Excel备份文件',
    '.bak': '临时备份文件bak'
    }
    del_userprofile = ['cookies', 'recent', 'Temporary Internet Files', 'Temp']
    del_windir = ['prefetch', 'temp']
    SYS_DRIVE = os.environ['systemdrive'] + '\\'
    USER_PROFILE = os.environ['userprofile']
    WIN_DIR = os.environ['windir']

    def del_dir_or_file(root):
        try:
            if os.path.isfile(root):
                os.remove(root)
                print ("file",root,"removed")
            elif os.path.isdir(root):
                os.rmdir(root)
                print("dir",root,"removed")

        except WindowsError:
            print("failure",root,"can't remove")

    def formatSize(b):
        try:
            kb = b // 1024
        except:
            print("传入字节格式不对")
            return "Error"
        if kb > 1024:
            M = kb // 1024
            if M > 1024:
                G = M // 1024
                return "%dG" % G
            else:
                return "%dM" % M
        else:
            return "%dkb" % kb

    class DiskClean(object):
        def __init__(self):
            self.del_info = {}
            self.del_file_paths = []
            self.total_size = 0
            for i,j in del_extension.items():
                self.del_info[i] = dict(name = j,count = 0 )

        def scanf(self):
            for roots,dirs,files in os.walk(USER_PROFILE):
                for files_item in files:
                        file_extension = os.path.splitext(files_item)[1]
                if file_extension in self.del_info:
                        file_full_path = os.path.join(roots,files_item)
                        self.del_file_paths.append(file_full_path)
                        self.del_info[file_extension]['count'] += 1
                        self.total_size += os.path.getsize(file_full_path)

        def show(self):
            re = formatSize(self.total_size)
            for i in self.del_info:
                print(self.del_info[i]["name"],"共计",self.del_info[i]["count"],"个")
            return re

        def delete_files(self):
            for i in self.del_file_paths:
                print(i)
                del_dir_or_file(i)
    if __name__ == "__main__":
        print("初始化清理垃圾程序")
        cleaner = DiskClean()
        print("开始扫描垃圾文件请耐心等待\n")
        cleaner.scanf()
        print("扫描成功,结果如下")
        re = cleaner.show()
        cleaner.delete_files()
        back()

def 写入文件():
    print("开发中...")
    back()

def Windows修复():
    os.system("sfc /scannow")
    back()

def 随机字符生成():
    #生成字典a-z
    a=string.ascii_lowercase
    #生成字典0-9
    b=string.digits
    #生成字典A-Z
    c=string.ascii_uppercase
    #生成字典符号
    d=string.punctuation
    #生成字典所有
    f=a+b+c+d
    #输入需要生成的密码长度
    n=int(input('请输入需要生成的字符长度：'))
    #生成密码
    p=''
    for i in range(n):
        p+=f[random.randint(0,len(f)-1)]
    #输出密码
    print('生成的字符为：',p)
    #输出密码长度
    print('生成的字符长度为：',len(p))
    back()


def 关于():
    print('''
    medor
    Copyright 2020-2022 GONGYE Heyu
    版本22.0514''')
    back()

def cls():
    system('cls')

def back():
    input("按任意键返回")
    cls()
    apps()

start()