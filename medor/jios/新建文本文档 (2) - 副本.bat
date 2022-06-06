@echo off
Title 姬拟太美
Cls
systeminfo
cls
Echo 0.退出
Echo 1.电源
Echo 2.便捷查询
Echo 3.小功能
Set /p a=请输入数字来执行你的操作
If %a%==0 goto 0
If %a%==1 goto 1
If %a%==2 goto 2
If %a%==3 goto 3
Echo 输入错误，请重新输入！
Ping /n 2 127.0.0.1 >nul
Goto !
:0
Cls
Echo 感谢使用，再见！
Ping /n 2 127.0.0.1 >nul
Exit
:1
Cls
Echo 1.关机
Echo 2.重启
Echo 3.休眠
Echo 4.注销
Echo 5.返回菜单
Set /p !=请输入数字来执行你的操作
If %!%==1 goto !1
If %!%==2 goto !2
If %!%==3 goto !3
If %!%==4 goto !4
If %!%==5 goto !5
Cls
Echo 输入错误，请重新输入！
Ping /n 2 127.0.0.1 >nul
Goto 1
:!1
Shutdown -s -f -t 30
Cls
Echo 是否终止？如果终止关机请输入a 如果需要直接关机请输入b
Set /p C=请输入字母来执行你的操作
Cls
If %C%==a goto C1
If %C%==b goto C2
:!2
Cls
Shutdown -r -t 30
:!3
Cls
Shutdown -h -f
Goto !
:!4
Cls
Shutdown -l
Goto !
:!5
Goto !
:C1
Shutdown -a
Cls
Goto !
:C2
Shutdown -s -t 0
:2
Cls
Echo 1.IP地址查询
Echo 2.软件查询
Echo 3.未完善
Echo 4.返回菜单
Set /p @=请输入数字来执行你的操作
Cls
If %@%==1 goto @1
If %@%==2 goto @2
If %@%==4 goto @4
Cls
Echo 输入错误，请重新输入！
Ping /n 2 127.0.0.1 >nul
Goto 2
:@1
Cls
Ipconfig/all
Echo 按下任意键回到菜单
Pause>nul
Cls
Goto !
:@2
Cls
Echo 请输入目录来打开软件
Set /p @2.1=盘[c d e f……]
Set /p @2.2=下一目录
Set /p @2.3=下一目录
Set /p @2.4=下一目录
Set /p @2.5=下一目录
Set /p @2.6=下一目录
Set /p @2.7=下一目录
Set /p @2.8=下一目录
Set /p @2.9=下一目录
Set /p @2.10=下一目录
Set /p @2.11=下一目录
:@2start 
Start “:%@2.1%\%@2.2%\%@2.3%\%@2.4%\%@2.5%\%@2.6%\%@2.7%\%@2.8%\%@2.9%\%@2.10%\%@2.11%”
:@4
Cls
Goto !
:3
Cls
Echo 1.清理垃圾
Echo 2.写入文档
Echo 3.本地连接
Set /p #=请输入数字来执行你的操作
If %#%==1 goto #1
If %#%==2 goto #2
If %#%==3 goto #3
Cls
Echo 输入错误，请重新输入！
Ping /n 2 127.0.0.1 >nul
Goto 3
:#1
Cls
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
Goto !
:#2
Echo 请输入文件名
Set /p biaoti=
Echo 请输入后缀名
Set /p houzhui=
Echo 输入完成！
Echo 按任意键开始输入文本
Pause>nul
Cls
Echo 输入完成请打ok以便结束打字
Goto #2.2.1
:#2.2.1
Set /p batdazi=
If “%batdazi%”==”ok” goto !
Echo ----------------------- >>%biaoti%.%houzhui%
Echo %batdazi%>>%biaoti%.%houzhui%
Goto #2.2.1
:#3
Cls
Echo 1.本地连接/开启
Echo 2.本地连接/关闭
Set /p KEY=请输入数字来执行你的操作
If %KEY% == 1 goto #2.3.1
If %KEY% == 2 goto #2.3.2
Cls
Echo 输入错误，请重新输入！
Ping /n 2 127.0.0.1 >nul
Goto #3
:#2.3.2
Cls
Echo 已经禁用本地连接。
Netsh interface set interface name=”以太网” admin=DISABLED
Ping /n 2 127.0.0.1 >nul
Goto !
:#2.3.1 
Cls
Echo 正在启用本地连接…
Netsh interface set interface name=”以太网” admin=ENABLED
Ping /n 2 127.0.0.1 >nul
Goto !