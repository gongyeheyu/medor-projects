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
    text = tkinter.Label(ab, text = mainame + '_',fg = 'black')
    text.pack()
    text1 = tkinter.Label(ab, text = '版本 ' + ver,fg = 'black')
    text1.pack()
    text2 = tkinter.Label(ab, text = '2022 GONGYE Heyu SIPL22.704',fg = 'black')
    text2.pack()
    text3 = tkinter.Label(ab, text = 'gongyeheyu@outlook.com',fg = 'black')
    text3.pack()
    text4 = tkinter.Label(ab, text = uplog,fg = 'black')
    text4.pack()
    text5 = tkinter.Label(ab, text = '加载耗时' + loadt,fg = 'black')
    text5.pack()
    button = tkinter.Button(ab, text="      ", command = light)
    button.pack()
    
def desk():
    global ver
    top=tkinter.Tk()
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
    done.title('medor-format' + '_' + ver)
    done = tkinter.Label(done, text='转换完成！')
    done.pack()
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
2022.07.21
    1.新增图形界面
    2.新增无数BUG qwq
    3.有一个彩蛋

2022.07.18'''

t = time.time()
loadt = str(t-t0)

desk()