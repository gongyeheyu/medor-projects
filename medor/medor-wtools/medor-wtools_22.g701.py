# -*- coding: utf-8 -*-
import numbers
from os import system
import socket
import re, os 
import string
import random
from time import time, localtime, sleep

def start():
    cls()
    print ('''0.退出
1.应用程序
2.时钟''')
    startcho = int(input("请输入数字来执行你的操作"))
    if startcho == 0:
        cls()   #220701 GONGYE Heyu
        print("感谢使用,再见")
    elif  startcho == 1:
        cls()   #220701 GONGYE Heyu
        apps()
    elif startcho == 2:
        cls()   #220701 GONGYE Heyu
        clock()
    else:
         input("输入错误")
         cls()
         start()

def apps():
    cls()
    print('''
    1.IP地址
    2.软件查询
    3.本地连接
    4.清理垃圾
    5.写入文件
    6.Windows修复
    7.开始
    8.关于
    9.随机字符生成
    10.时钟''')
    #“时钟” 220701 GONGYE Heyu
    appscho = int(input("请输入"))
    int(appscho)
    if appscho == 1:
        IP地址()
    elif appscho == 2:
        软件查询()
    elif appscho == 3:
        #本地连接()
        cls()
        网络信息()  #220701 GONGYE Heyu
    elif appscho == 4:
        cls()   #220701 GONGYE Heyu
        清理垃圾()
    elif appscho == 5:
        #写入文件()
        文件编辑()  #220701 GONGYE Heyu
    elif appscho == 6:
        Windows修复()
    elif appscho == 7:
        start()
    elif appscho == 8:
        关于()
    elif appscho == 9:
        随机字符生成()
    elif appscho == 10:
        clock()    #220701 GONGYE Heyu
    else :
        input("输入错误")
        cls()
        apps()

def IP地址():
    cls()
    # 获取本机计算机名称
    hostname = socket.gethostname()
    # 获取本机ip
    ip = socket.gethostbyname(hostname)
    print("主机名" + hostname)
    print("IP地址" + ip)
    back()

def 软件查询():
    cls()
    print("开发中...")
    back()   
    
#def 本地连接(): 
#   print("开发中...")
#220701 GONGYE Heyu

def 网络信息():
    cls()
    print(os.system('netstat -sera'))
    print(os.system('ipconfig /all'))
    back()
#220701 GONGYE Heyu

def 清理垃圾():
    cls()
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

#def 写入文件():
#   print("开发中...")
#    back()

def 文件编辑():
    cls()
    w = input("请输入路径")
    i = input('''n.新建文件
    o.读取文件
    l.列出文件
    d.删除文件
    b.返回''')
    if i == 'n':
        f = open(w, 'w')
        f.close()
        print("文件创建完成")
        文件编辑()
    elif i == 'o':
        f = open(w, 'r')
        print(f.read())
        f.close()
        文件编辑()
    elif i == 'l':
        print(os.system('dir ' + w))
        文件编辑()
    elif i == 'd':
        os.remove(w)
        print("文件删除完成")
        文件编辑()
    elif i == 'b':
        back()
    else:
        print("输入错误")
        文件编辑()
    #220701 GONGYE Heyu


def Windows修复():
    cls()
    os.system("sfc /scannow")
    back()

def 随机字符生成():
    cls()
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

def clock():
    cls()
    class Clock(object):
        """数字时钟"""
        def __init__(self,hour=0,minute=0,second=0):
            """
            构造器
            :param hour: 时
            :param minute: 分
            :param second: 秒
            """
            self._hour=hour
            self._minute=minute
            self._second=second
        @classmethod
        def now(cls):
            ctime = localtime(time())
            return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
        def run(self):
            """走字"""
            self._second+=1
            if self._second==60:
                self._second=0
                self._minute+=1
                if self._minute == 60:
                    self._minute=0
                    self._hour+=1
                    if self._hour==24:
                        self._hour=0           
        """时钟打印"""
        def __str__(self):
            cls()
            return '%02d:%02d:%02d' % (self._hour,self._minute,self._second)
    def main():
        clock=Clock.now()
        while True:
            print(clock)
            sleep(1)
            clock.run()
    if __name__ == '__main__':
        main()

def 关于():
    cls()
    print('''
    medor/wtools
    Copyright 2020-2022 GONGYE Heyu
    版本22.701
    
    a.查看许可证
    b.更新日志
    c.返回''')
    i = input()
    if i == "a":
        cls()
        print(license)
        back()
    elif i == "b":
        cls()
        print(uplog)
        back()
    else :
        back()

def cls():
    system('cls')

def back():
    input("按任意键返回")
    cls()
    apps()

uplog = '''
更新日志：
2022.07.01
1.新增网络信息，文件编辑，时钟，开源许可证
2.新增无数BUG  qwq
'''

license = '''
严格知识产权许可证（试用）
版本 22.704

注意：本文中的“您”包括任何有独立思想的个人、组织、机构、社会团体、公司、政府、任何计算机程序。

1. 在使用此许可证时，您必须遵守当地法律法规，否则此许可证无效；如果针对本作品出现任何法律纠纷，则需要通过当地法律法规来解决。

2. 您可以自由复制、散布、展示及演出本著作，但必须注明原作者及各衍生版本作者（以下简称“作者”）（“衍生版本”不包括与该著作及其衍生版本分离的著作，或仅与该著作及其衍生版本的接口链接或按名称绑定的著作）。

3. 若您想要散布修改后的本著作或散布引用本著作大于等于10%的著作（以下简称“新著作”），只有在遵守与本著作相同的授权协议或不相冲突的多个协议（以下简称“这些协议”）下，您才能散布它（如果您不希望遵守这些协议，请阅读第4条）。您必须按照原作者或原作者指定的授权人的许可（以下简称“授权”）所指定的方式，保留其原作者及所涉及到的各个分支内的各衍生版本作者姓名标识。

4. 如果您不希望您的新著作遵守这些协议，您必须获得作者及一半及以上该著作贡献者（如果有）的许可，并由作者决定是否需要注明作者及缴纳许可费用等。

5. 如果您对您改变、转变或改作之后的作品以盈利为目的使用，如添加任何形式的广告等使用此著作来获利的行为，您必须获得作者的许可，并由作者决定是否注明作者及缴纳许可费用等。

6. 如果您遵守这些协议，在本著作中涉及到的所有专利的使用均无需获得作者的许可，但只可以在本著作及其各衍生版本中使用；如果您不希望遵守这些协议，您需要获得原作者及此专利持有人的许可并由原作者及此专利持有人决定是否注明原作者及此专利持有人及缴纳许可费用等。

7. 允许使用本著作进行计算机程序的训练，但此计算机程序和训练结果必须遵守本协议；如果此计算机程序不希望遵守本协议，您需要获得原作者及一半以上该著作贡献者（如果有）的许可，并由作者决定是否需要注明作者及缴纳许可费用等。

颁发者：GONGYE Heyu



Strict Intellectual Property License (Trial)
Version 22.704

Note: "You" in this article includes any independent thinking individual, organization, institution, social group, company, government, any computer program.

1. When using this license, you must abide by local laws and regulations, otherwise this license is invalid; if there is any legal dispute against this work, it needs to be resolved through local laws and regulations.

2. You are free to copy, distribute, display and perform this work, but you must indicate the original author and the author of each derivative version (hereinafter referred to as "author") ("Derivative version" does not include the work separated from the work and its derivative versions. , or a work that is only linked or bound by name to the interface of that work and its derivatives).

3. If you want to distribute the revised work or a work that cites 10% or more of this work (hereinafter referred to as "new work"), only if you comply with the same license agreement as this work or multiple non-conflicting agreements (hereinafter referred to as "these agreements"), you can distribute it (if you do not wish to abide by these agreements, please read Section 4). You must retain the original author and the author's name identification of each derivative version in each branch involved in the manner specified in the license of the original author or the licensor designated by the original author (hereinafter referred to as "authorization").

4. If you do not want your new work to comply with these agreements, you must obtain the permission of the author and half or more of the contributors to the work (if any), and the author decides whether to indicate the author and pay the license fee.

5. If you use your modified, transformed or modified work for profit, such as adding any form of advertising, you must obtain the author's permission, and the author decides whether to indicate Author and payment of license fees, etc.

6. If you comply with these agreements, the use of all patents involved in this work does not require the permission of the author, but can only be used in this work and its derivative versions; if you do not wish to comply with these agreements, you need to Obtain the permission of the original author and the patent holder and decide whether to indicate the original author and the patent holder and pay the license fee, etc.

7. It is allowed to use this work for computer program training, but the computer program and training results must comply with this agreement; if this computer program does not wish to comply with this agreement, you need to obtain the original author and more than half of the contributors to the work (if any) It is up to the author to decide whether to indicate the author and pay the license fee.

Issued by:GONGYE Heyu

'''

start()