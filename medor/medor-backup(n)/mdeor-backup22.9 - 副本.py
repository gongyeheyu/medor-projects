#coding:utf-8
# 全局设置
import os
import sys
import time
import calendar

def help():
    print('''medor 22.w3029帮助
    create                     新建还原点
    restore                    还原到指定还原点
    del                        删除还原点''')

def create():
    cmd3 = sys.argv[3];
    if cmd3 == None:
        t = calendar.timegm(time.gmtime())
    else:
        t = cmd3
    # 读取要压缩的文件
    cmd2 = sys.argv[2];
    filename = cmd2
    # 调用压缩指令
    os.system('tar -czf ' + filename + '.tar.gz ' + filename)
    
#删除还原点
def del_restore():
    cmd3 = sys.argv[3];
    if cmd3 == None:
        t = calendar.timegm(time.gmtime())
    else:
        t = cmd3
    # 读取要压缩的文件
    cmd2 = sys.argv[2];
    filename = cmd2
    # 调用压缩指令
    os.system('rm -rf ' + filename + '.tar.gz')

#还原到指定还原点
def restore():
    cmd3 = sys.argv[3];
    if cmd3 == None:
        t = calendar.timegm(time.gmtime())
    else:
        t = cmd3
    # 读取要压缩的文件
    cmd2 = sys.argv[2];
    filename = cmd2
    # 调用压缩指令
    os.system('tar -xzf ' + filename + '.tar.gz')

def st():
    cmd1 = sys.argv[1];
    print('''medor 版本22.w0329
    输入“help”获取帮助''')
    if cmd1 == help:
        help()
    elif cmd1 == create:
        create()
st()

