# -*- coding: utf-8 -*-
import numbers
from os import system
import socket
import re, os 

def start():
    cls()
    print ("0.退出")
    print ("1.应用程序")
    startcho = input("请输入数字来执行你的操作")
    start = ['0','1']
    if startcho == start[0]:
        print("感谢使用,再见")
    if startcho == start[1]:
        cls()
        apps()    

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
    8.关于''')
    appscho = int(input("请输入"))
    int(appscho)
    if appscho == 1:
        IP地址()
    elif appscho == 2:
        软件查询()
    elif appscho == 3:
        本地连接()
    elif appscho == 4:
        清理垃圾()
    elif appscho == 5:
        写入文件()
    elif appscho ==6:
        Windows修复()
    elif appscho == 7:
        start()
    elif appscho == 8:
        关于()
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
    
def 本地连接():
    cls() 
    os.system("ipconfig /all")
    back()

def 清理垃圾():
    cls()
    os.system('''Cls
                 Echo 准备清理系统垃圾….
                 Ping /n 3 127.0.0.1 >nul
                 Del /f /s /q %systemdrive%\*.tmp&del /f /s /q %systemdrive%\*._mp 
                 Del /f /s /q %systemdrive%\*.log&del /f /s /q %systemdrive%\*.gid 
                 Del /f /s /q %systemdrive%\*.chk&del /f /s /q %systemdrive%\*.old 
                 Del /f /s /q %systemdrive%\recycled\*.*&del /f /s /q %windir%\*.bak 
                 Del /f /s /q %windir%\prefetch\*.*&rd /s /q %windir%\temp & md %windir%\temp 
                 Del /f /q %userprofile%\cookies\*.*&del /f /q %userprofile%\recent\*.* 
                 Del /f /s /q “%userprofile%\Local Settings\Temporary Internet Files\*.*” 
                 Del /f /s /q “%userprofile%\Local Settings\Temp\*.*”
                 Del /f /s /q “%userprofile%\recent\*.*” 
                 Cls
                 Echo 清理完成!
                 Ping /n 2 127.0.0.1 >nul
                 ''')
    back()

def 写入文件():
    cls()
    print("开发中...")
    back()

def Windows修复():
    cls()
    os.system("sfc /scannow")
    back()

def 关于():
    cls()
    print('''
    MEDOR FOR Windows10
    Copyright 2020-2022 GONGYE Heyu
    版本 22.win.build@m2h
    gongyeheyu.github.io/medor''')
    back()

def cls():
    system('cls')

def back():
    input("按任意键返回")
    cls()
    apps()

start()