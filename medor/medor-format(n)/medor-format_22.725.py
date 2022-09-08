#这是一个图形化的格式转换，其实就是ffmpeg套壳
#在Windows正常运行需要将ffmpeg.exe添加到PATH

import time
t0 = time.time()
from ffmpy import FFmpeg
import os
import tkinter

def format():
    global inmat
    global out
    formattop = tkinter.Tk()
    formattop.title(mainame + '_' + ver + '/format')
    formattop.geometry('720x360')
    text = tkinter.Label(formattop, text = mainame + '_' + ver + '/format',fg = 'black')
    text.pack()
    #文本框输入源文件名称
    inmat = tkinter.Label(formattop, text='输入源文件名称：')
    inmat.pack()
    inmat = tkinter.Entry(formattop)
    inmat.pack()
    #文本框输入要转换的格式
    out = tkinter.Label(formattop, text='输入要转换的格式：')
    out.pack()
    out = tkinter.Entry(formattop)
    out.pack()
    #按下按钮开始转换
    def formating():
        inmatlist = inmat.get()
        (name, ext) = os.path.splitext(inmatlist)
        ff = FFmpeg(inputs={str(inmat.get()): None}, outputs={name +'.' + str(out.get()): None})
        ff.run()
        done()
    button = tkinter.Button(formattop, text="开始", command = formating)
    button.pack()
    formattop.mainloop()

def vtranscode():
    global inmat
    global out
    vtrantop = tkinter.Tk()
    vtrantop.title(mainame + '_' + ver + '/vtranscode')
    vtrantop.geometry('720x360')
    text = tkinter.Label(vtrantop, text = mainame + '_' + ver + '/vtranscode',fg = 'black')
    text.pack()
    #文本框输入源文件名称
    inmat = tkinter.Label(vtrantop, text='输入源文件名称：')
    inmat.pack()
    inmat = tkinter.Entry(vtrantop)
    inmat.pack()
    #文本框输入要转换的格式
    out = tkinter.Label(vtrantop, text='输入要转换的视频编码：')
    out.pack()
    out = tkinter.Entry(vtrantop)
    out.pack()
    def vtraning():
        inmatlist = inmat.get()
        (name, ext) = os.path.splitext(inmatlist)
        outt = out.get()
        ff = FFmpeg(inputs={str(inmat.get()): None}, 
        outputs={name + '(1)' + ext: '-c:v ' + outt})
        ff.run()
        done()
    button = tkinter.Button(vtrantop, text="开始", command = vtraning)
    button.pack()

def atranscode():
    global inmat
    global out
    atrantop = tkinter.Tk()
    atrantop.title(mainame + '_' + ver + '/atranscode')
    atrantop.geometry('720x360')
    text = tkinter.Label(atrantop, text = mainame + '_' + ver + '/atranscode',fg = 'black')
    text.pack()
    #文本框输入源文件名称
    inmat = tkinter.Label(atrantop, text='输入源文件名称：')
    inmat.pack()
    inmat = tkinter.Entry(atrantop)
    inmat.pack()
    #文本框输入要转换的格式
    out = tkinter.Label(atrantop, text='输入要转换的音频编码：')
    out.pack()
    out = tkinter.Entry(atrantop)
    out.pack()
    def atraning():
        inmatlist = inmat.get()
        (name, ext) = os.path.splitext(inmatlist)
        outt = out.get()
        ff = FFmpeg(inputs={str(inmat.get()): None}, 
        outputs={name + '(1)' + ext: '-c:a ' + outt})
        ff.run()
        done()
    button = tkinter.Button(atrantop, text="开始", command = atraning)
    button.pack()

def about():
    ab = tkinter.Tk()
    ab.title('medor-format' + '_' + ver + '/about')
    ab.geometry('720x360')
    text = tkinter.Label(ab, text = mainame + '_', fg = 'black')
    text.pack()
    text1 = tkinter.Label(ab, text = '版本 ' + ver,fg = 'black')
    text1.pack()
    text2 = tkinter.Label(ab, text = '2022 GONGYE Heyu SIPL22.704', fg = 'black')
    text2.pack()
    text3 = tkinter.Label(ab, text = 'gongyeheyu@outlook.com', fg = 'black')
    text3.pack()
    text4 = tkinter.Label(ab, text = uplog,fg = 'black')
    text4.pack()
    text5 = tkinter.Label(ab, text = '加载耗时' + str(t-t0), fg = 'black')
    text5.pack()
    button = tkinter.Button(ab, text="查看许可证", command = licen)
    button.pack()
    button1 = tkinter.Button(ab, text="      ", command = light)
    button1.pack()
    
def desk():
    global ver
    top = tkinter.Tk()
    top.title('medor-format' + '_' + ver)
    top.geometry('720x360')
    text = tkinter.Label(top, text="medor-format" + '_' + ver,fg = 'black')
    text.pack()
    #按钮“格式转换”调用函数format
    button1 = tkinter.Button(top, text='格式转换', command=format)
    button1.pack()
    #按钮“视频转码”调用函数vtranscode
    button2 = tkinter.Button(top, text='视频转码', command=vtranscode)
    button2.pack()
    #按钮“音频转码”调用函数atranscode
    button3 = tkinter.Button(top, text='音频转码', command=atranscode)
    button3.pack()
    #按钮“关于”调用函数about
    button4 = tkinter.Button(top, text='关于', command=about)
    button4.pack()
    #按钮“退出”调用函数quit
    button5 = tkinter.Button(top, text='退出', command=top.quit)
    button5.pack()
    top.mainloop()

def done():
    done = tkinter.Tk()
    done.geometry('360x180')
    done.title('medor-format' + '_' + ver)
    done = tkinter.Label(done, text='转换完成！')
    done.pack()
    button = tkinter.Button(done, text='关闭', command = done.quit)
    button.pack()
    done.mainloop()

def light():
    light = tkinter.Tk()
    light.title('light')
    light.geometry('720x360')
    text = tkinter.Label(light, text='''
    呐，你看到啦
    这个，大概可以叫彩蛋吧
    如你所见，这东西BUG相当多
    其实，为啥要写这东西呢
    编程，或者应该说是电脑
    几乎成了我唯一活下去的希望了...
    嗯，不说了，再说又想哭了qwq
    所以，可以帮我维护一下代码吗？
    麻烦了！
    ''',fg = 'black')
    text.pack()

mainame='medor-format'
ver='22.720'
uplog = '''
更新日志:
2022.07.25
    1.新增查看许可证
    2.优化代码
    3.还有亿些BUG尚未解决

2022.07.21
    1.新增图形界面
    2.新增无数BUG qwq
    3.有一个彩蛋

2022.07.18'''

license = '''严格知识产权许可证（试用）
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

def licen():
    license = tkinter.Tk()
    license.title('medor-format' + '_' + ver)
    license.geometry('720x360')
    text = tkinter.Label(license, text=license)
    text.pack()

t = time.time()

desk()