import os
import time
import calendar
import sys

if __name__ == '__main__':
    # 读取命令行参数
    command = sys.argv[1];
    # 设置zip路径
    zipPath = 'C:\Program Files\7-Zip\7z.exe'
    # 如果是cp命令 执行压缩程序
    if command == "cp":
        # 读取要压缩的文件
        filename = sys.argv[2];
        # 获取当前时间
        t = calendar.timegm(time.gmtime())
        # 调用压缩指令
        cmd = f'{zipPath} a {filename}_{t}.7z {filename} -mx=9'
        os.system(cmd)
    # 如果是ex命令 执行解压缩程序
    elif command == "ex" and len(sys.argv) == 4:
        # 获取文件名
        filename = sys.argv[2];
        # 获取还原点时间
        t = sys.argv[3]
        # 获取当前所有文件
        files = os.listdir('.');
        # 遍历
        for i in files:
            # 如果文件是7z文件
            if i.startswith(filename) and i.endswith("7z"):
                # 且在还原时间点钱
                if int(i.split('_')[1].split('.')[0]) <= int(t):
                    # 执行解压缩程序
                    cmd = f'{zipPath} x -y {i} -o.'
                    os.system(cmd)
    #  如果是ex命令 执行解压缩程序
    elif command == "ex":
        # 获取文件名
        filename = sys.argv[2];
        # 获取所有路径
        files = os.listdir('.');
        # 遍历
        for i in files:
            # 如果是7z文件
            if i.startswith(filename) and i.endswith("7z"):
                # 解压缩
                cmd = f'{zipPath} x -y {i} -o.'
                os.system(cmd)

