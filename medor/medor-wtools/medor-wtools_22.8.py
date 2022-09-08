# -*- coding: utf-8 -*-
def t0():
    #获取现在时间戳
    import time
    t0 = time.time()
    return t0
ti0 = t0()

ver = '22.818'
mainame = 'medor-wtools'
mainpath = '\AppData\Roaming\medor\wtools'

import tkinter
def start():
    log('start')
    start = tkinter.Tk()
    start.title(mainame + '_' + ver)
    start.geometry('720x360')
    text = tkinter.Label(start, text=mainame + '_' + ver,fg = 'black')
    text.pack()
    button0 = tkinter.Button(start, text='IP地址', command=ipsearch)
    button0.pack()
    button1 = tkinter.Button(start, text='软件查询', command=appsearch)
    button1.pack()
    button2 = tkinter.Button(start, text='网络信息', command=netinfo)
    button2.pack()
    button3 = tkinter.Button(start, text='清理垃圾', command=clean)
    button3.pack()
    button5 = tkinter.Button(start, text='Windows修复', command=winfit)
    button5.pack()
    button6 = tkinter.Button(start, text='随机字符生成', command=rcg)
    button6.pack()
    button7 = tkinter.Button(start, text='时钟', command=clock)
    button7.pack()
    button8 = tkinter.Button(start, text='关于', command=about)
    button8.pack()
    button9 = tkinter.Button(start, text='退出', command=quit)
    button9.pack()
    start.mainloop()

def ipsearch():
    log('ipsearch')
    import socket
    # 获取本机名称
    hostname = socket.gethostname()
    # 获取本机ip
    ip = socket.gethostbyname(hostname)
    ipsearch = tkinter.Tk()
    ipsearch.title(mainame + '_' + ver + '/ipsearch')
    ipsearch.geometry('720x360')
    text0 = tkinter.Label(ipsearch, text=mainame + '_' + ver + '/ipsearch',fg = 'black')
    text0.pack()
    text1 = tkinter.Label(ipsearch, text='本机名称:' + hostname,fg = 'black')
    text1.pack()
    text2 = tkinter.Label(ipsearch, text='本机ip:' + ip,fg = 'black')
    text2.pack()
    ipsearch.mainloop()

def appsearch():
    log('appsearch')
    appsearch = tkinter.Tk()
    appsearch.title(mainame + '_' + ver + '/appsearch')
    appsearch.geometry('720x360')
    text0 = tkinter.Label(appsearch, text=mainame + '_' + ver + '/appsearch',fg = 'black')
    text0.pack()
    text1 = tkinter.Label(appsearch, text='此功能尚未开放...',fg = 'black')
    text1.pack()
    appsearch.mainloop()

def netinfo():
    log('netinfo')
    import os
    net = os.system('netstat -sera')
    ipc = os.system('ipconfig /all')
    netinfo = tkinter.Tk()
    netinfo.title(mainame + '_' + ver + '/netinfo')
    netinfo.geometry('720x360')
    text0 = tkinter.Label(netinfo, text=mainame + '_' + ver + '/netinfo',fg = 'black')
    text0.pack()
    text1 = tkinter.Label(netinfo, text=net,fg = 'black')
    text1.pack()
    text2 = tkinter.Label(netinfo, text=ipc,fg = 'black')
    text2.pack()
    netinfo.mainloop()

def clean():
    log('clean')
    clean = tkinter.Tk()
    clean.title(mainame + '_' + ver + '/clean')
    clean.geometry('720x360')
    text0 = tkinter.Label(clean, text=mainame + '_' + ver + '/clean',fg = 'black')
    text0.pack()
    text1 = tkinter.Label(clean, text='此功能尚未开放，估计以后也不会开放，这个问题很多，有兴趣可以去代码里看看',fg = 'black')
    text1.pack()
    clean.mainloop()

def 清理垃圾():
    log('清理垃圾')
    import os
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
        print("扫描成功，结果如下")
        re = cleaner.show()
        cleaner.delete_files()

def winfit():
    log('winfit')
    def fit():
        log('winfitted')
        import os
        os.system("sfc /scannow")
        done()
    winfit = tkinter.Tk()
    winfit.title(mainame + '_' + ver + '/winfit')
    winfit.geometry('720x360')
    text0 = tkinter.Label(winfit, text=mainame + '_' + ver + '/winfit',fg = 'black')
    text0.pack()
    button0 = tkinter.Button(winfit, text='开始', command=fit)
    button0.pack()
    winfit.mainloop()
        

def rcg():
    log('rcg')
    rcg = tkinter.Tk()
    rcg.title(mainame + '_' + ver + '/rcg')
    rcg.geometry('720x360')
    text0 = tkinter.Label(rcg, text=mainame + '_' + ver + '/rcg',fg = 'black')
    text0.pack()
    text = tkinter.Label(rcg, text='输入要生成的字符长度：')
    text.pack()
    text = tkinter.Entry(rcg)
    text.pack()
    t = int(text.get())
    def rcgo():
        log('rcgo')
        import string
        import random
        str = ''
        chars = string.ascii_letters + string.digits + string.punctuation
        for i in range(t):
            str += random.choice(chars)
        rcgo = tkinter.Tk()
        rcgo.title(mainame + '_' + ver + '/rcg')
        rcgo.geometry('360x180')
        text0 = tkinter.Label(rcgo, text=mainame + '_' + ver + '/rcg',fg = 'black')
        text0.pack()
        text = tkinter.Label(rcgo, text=str)
        text.pack()
        rcgo.mainloop()
    button = tkinter.Button(rcg, text='开始', command=rcgo)
    button.pack()
    rcg.mainloop()

def clock():
    log('clock')
    import turtle
    import datetime
    # 抬起画笔，向前运动一段距离放下
    def skip(step):
        turtle.penup()
        turtle.forward(step)
        turtle.pendown()
 
    def mkHand(name, length):
        # 注册Turtle形状，建立表针Turtle
        turtle.reset()
        # 先反向运动一段距离，终点作为绘制指针的起点
        skip(-length * 0.1)
        # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
        turtle.begin_poly()
        turtle.forward(length * 1.1)
        # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
        turtle.end_poly()
        # 返回最后记录的多边形。
        handForm = turtle.get_poly()
        turtle.register_shape(name, handForm)
 
    def init():
        global secHand, minHand, houHand, printer
        # 重置Turtle指向北
        turtle.mode("logo")
        # 建立三个表针Turtle并初始化
        mkHand("secHand", 135)
        mkHand("minHand", 125)
        mkHand("houHand", 90)
        secHand = turtle.Turtle()
        secHand.shape("secHand")
        minHand = turtle.Turtle()
        minHand.shape("minHand")
        houHand = turtle.Turtle()
        houHand.shape("houHand")
 
        for hand in secHand, minHand, houHand:
            hand.shapesize(1, 1, 3)
            hand.speed(0)
 
        # 建立输出文字Turtle
        printer = turtle.Turtle()
        # 隐藏画笔的turtle形状
        printer.hideturtle()
        printer.penup()
 
    # 绘制表盘
    def setupClock(radius):
        # 建立表的外框
        turtle.reset()
        turtle.pensize(7)
        for i in range(60):
            # 向前移动半径值
            skip(radius)
            if i % 5 == 0:
                # 画长刻度线
                turtle.forward(20)
                # 回到中心点
                skip(-radius - 20)
                # 移动到刻度线终点
                skip(radius + 20)
                # 下面是写表盘刻度值,为了不与划线重叠，所以对于特殊位置做了处理
                if i == 0:
                    turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
                elif i == 30:
                    skip(25)
                    turtle.write(int(i/5), align="center", font=("Courier", 14, "bold"))
                    skip(-25)
                elif (i == 25 or i == 35):
                    skip(20)
                    turtle.write(int(i/5), align="center", font=("Courier", 14, "bold"))
                    skip(-20)
                else:
                    turtle.write(int(i/5), align="center", font=("Courier", 14, "bold"))
                # 回到中心点
                skip(-radius - 20)
            else:
                # 画圆点
                turtle.dot(5)
                skip(-radius)
            # 顺时针移动6°
            turtle.right(6)
 
    def week(t):
        week = ["星期一", "星期二", "星期三",
                "星期四", "星期五", "星期六", "星期日"]
        return week[t.weekday()]
 
    def date(t):
        y = t.year
        m = t.month
        d = t.day
        return "%s %d%d" % (y, m, d)
 
    def tick():
        # 绘制表针的动态显示
        t = datetime.today()
        second = t.second + t.microsecond * 0.000001
        minute = t.minute + second / 60.0
        hour = t.hour + minute / 60.0
        secHand.setheading(6 * second)
        minHand.setheading(6 * minute)
        houHand.setheading(30 * hour)
 
        turtle.tracer(False)
        printer.forward(65)
        printer.write(week(t), align="center",
                      font=("Courier", 14, "bold"))
        printer.back(130)
        printer.write(date(t), align="center",
                      font=("Courier", 14, "bold"))
        printer.home()
        turtle.tracer(True)
        # 100ms后继续调用tick
        turtle.ontimer(tick, 100)
 
    def main():
        # 打开/关闭龟动画，并为更新图纸设置延迟。
        turtle.tracer(False)
        init()
        setupClock(160)
        turtle.tracer(True)
        tick()
        turtle.mainloop()
 
    if __name__ == "__main__":
        main()

def about():
    log('about')
    def licensegui():
        log('licensegui')
        licensegui = tkinter.Tk()
        licensegui.title(mainame + '_' + ver + '/license')
        licensegui.geometry('720x360')
        text4 = tkinter.Label(licensegui, text=mainame + '_' + ver + '/license',fg = 'black')
        text4.pack()
        text5 = tkinter.Label(licensegui, text=license,fg = 'black')
        text5.pack()
        licensegui.mainloop()
    def uplogui():
        log('uplogui')
        uplogui = tkinter.Tk()
        uplogui.title(mainame + '_' + ver + '/uplog')
        uplogui.geometry('720x360')
        text6 = tkinter.Label(uplogui, text=mainame + '_' + ver + '/uplog',fg = 'black')
        text6.pack()
        text7 = tkinter.Label(uplogui, text=uplog,fg = 'black')
        text7.pack()
        uplogui.mainloop()
    def loadtime():
        log('loadtime')
        loadtime = tkinter.Tk()
        loadtime.title(mainame + '_' + ver + '/loadtime')
        loadtime.geometry('720x360')
        text8 = tkinter.Label(loadtime, text=mainame + '_' + ver + '/loadtime',fg = 'black')
        text8.pack()
        text9 = tkinter.Label(loadtime, text=ti-ti0,fg = 'black')
        text9.pack()
        loadtime.mainloop()
    def aboutcodergui():
        log('aboutcodergui')
        aboutcodergui = tkinter.Tk()
        aboutcodergui.title(mainame + '_' + ver + '/aboutcoder')
        aboutcodergui.geometry('720x360')
        text10 = tkinter.Label(aboutcodergui, text=mainame + '_' + ver + '/aboutcoder',fg = 'black')
        text10.pack()
        text11 = tkinter.Label(aboutcodergui, text=aboutcoder,fg = 'black')
        text11.pack()
        aboutcodergui.mainloop()
    about = tkinter.Tk()
    about.title(mainame + '_' + ver + '/about')
    about.geometry('720x360')
    text0 = tkinter.Label(about, text=mainame + '_' + ver + '/about',fg = 'black')
    text0.pack()
    text1 = tkinter.Label(about, text=mainame,fg = 'black')
    text1.pack()
    text2 = tkinter.Label(about, text='Copyright 2020-2022 GONGYE Heyu All rights reserved',fg = 'black')
    text2.pack()
    text3 = tkinter.Label(about, text='版本:' + ver,fg = 'black')
    text3.pack()
    button0 = tkinter.Button(about, text='查看许可证', command=licensegui)
    button0.pack()
    button1 = tkinter.Button(about, text='更新日志', command=uplogui)
    button1.pack()
    button2 = tkinter.Button(about, text='加载耗时', command=loadtime)
    button2.pack()
    button3 = tkinter.Button(about, text='关于作者', command=aboutcodergui)
    button3.pack()
    about.mainloop()

def done():
    log('done')
    done = tkinter.Tk()
    done.geometry('360x180')
    done.title('medor-format' + '_' + ver)
    done = tkinter.Label(done, text='完成',fg = 'black')
    done.pack()
    button = tkinter.Button(done, text='关闭', command = done.quit)
    button.pack()
    done.mainloop()

def log(s):
    import os
    import time
    userpath = (os.path.expanduser('~'))
    if not os.path.exists(userpath + mainpath):
        os.mkdir(userpath + mainpath)
    f = open(userpath + mainpath + '\log.txt' , 'a')
    f.write(time.strftime('%Y-%m-%d-%H-%M-%S') + ':' + s + '\r\n')
    f.close()

aboutcoder = '''
GONGYE Heyu
联系方式:gongyeheyu@outlook.com'''

uplog = '''
更新日志：
2022.8.18
1.变成了GUI软件
2.改文本时钟为GUI时钟
3.弃用了“文件编辑”
4.几乎重写了所有代码
5.新增了“关于作者”界面
6.新增操作日志，目录: AppData\Roaming\medor\wtools\log.txt
6.优化了代码
7.新增无数BUG  qwq

2022.07.17
1.在你们看不见的地方优化了代码，但应该是个负优化，因为优化后比没有优化更慢

2022.07.16
1.修改了back函数，使其可以直接返回上一级菜单
2.改“本地连接”为“网络信息”
3.新增加载时间
4.新增无数BUG  qwq

2022.07.01
1.新增网络信息，文件编辑，时钟，开源许可证
2.新增无数BUG  qwq'''

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

Issued by:GONGYE Heyu'''

def t():
    import time
    t = time.time()
    return t
ti = t()

log('open')
start()