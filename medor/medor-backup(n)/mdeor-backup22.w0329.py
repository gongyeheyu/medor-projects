if __name__ == '__main__':
    #coding:utf-8
    # 全局设置
    import os
    import sys
    import time
    import calendar
    zipPath = 'C:\Program Files\7-Zip\7z.exe'
    cmd1 = sys.argv[1];
    cmd2 = sys.argv[2];
    cmd3 = sys.argv[3];

    def help():
        print('''medor 22.w3029帮助
        create                     新建还原点
        restore                    还原到指定还原点
        del                        删除还原点''')

    def create():
        if cmd3 == None:
            t = calendar.timegm(time.gmtime())
        else:
            t = cmd3
        # 读取要压缩的文件
        filename = sys.argv[2];
        # 调用压缩指令
        cmdo = f'{zipPath} a {filename}_{t}.7z {filename} -mx=9'
        os.system(cmdo)

    def st():
        print('''medor 版本22.w0329
        输入“help”获取帮助''')
        cmd1 = sys.argv[1];
        if cmd1 == help:
            help()
        elif cmd1 == create:
            create()
st()