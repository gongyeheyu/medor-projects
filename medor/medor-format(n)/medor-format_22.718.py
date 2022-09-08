# -*- coding: utf-8 -*-
import time
t0 = time.time()
from ffmpy import FFmpeg
from os import system
import sys

def start():
    cls()
    print('''
    1.格式转换
    2.视频转码
    3.音频转码
    4.关于''')
    startcho = int(input("请输入数字来执行你的操作"))
    if startcho == 1:
        format()
    elif startcho == 2:
        vtranscode()
    elif startcho == 3:
        atranscode()
    elif startcho == 4:
        about()
    else:
        input("输入错误")
        cls()
        start()

def format():
    cls()
    inmat = input('输入源文件名称：')
    out = input('输入要转换的格式：')
    inmatlist = inmat.split('.')
    ff = FFmpeg(inputs={inmat: None}, outputs={inmatlist[-2] +'.' + out: None})
    ff.run()
    print('转换完成！')
    back(1)

def vtranscode():
    cls()
    inmat = input('输入源文件名称：')
    out = input('输入要转换的视频编码：')
    inmatlist = inmat.split('.')
    ff = FFmpeg(inputs={inmat: None}, 
    outputs={inmatlist[-2] + '(1).' + inmatlist[-1]: '-c:v ' + out})
    ff.run()
    print('转换完成！')
    back(1)

def atranscode():
    cls()
    inmat = input('输入源文件名称：')
    out = input('输入要转换的音频编码：')
    inmatlist = inmat.split('.')
    ff = FFmpeg(inputs={inmat: None}, 
    outputs={inmatlist[-2] + '(1).' + inmatlist[-1]: '-c:a ' + out})
    ff.run()
    print('转换完成！')
    back(1)

def about():
    cls()
    print('''
    medor-wtools
    2022 GONGYE Heyu SIPL22.704
    版本 22.718
    
    更新日志:
    2022.07.18''')
    print('加载耗时')
    global t0
    global t
    print(t - t0)
    back(1)

def cls():
    system('cls')

def back(where):
    w = sys._getframe(1).f_code.co_name
    #where=0为直接返回主菜单，where=1为询问后返回主菜单#
    #where=2为直接返回上一级菜单,where=3为询问后返回上一级菜单
    if where == 0:
        cls() 
        start()
    elif where == 1:
        input("按任意键返回")
        cls()
        start()
    elif where == 2:
        cls()
        #调用w中的函数名
        globals()[w]()
    elif where == 3:
        input("按任意键返回")
        cls()
        globals()[w]()
    else:
        print("输入错误")
        back(3)

t = time.time()

start()