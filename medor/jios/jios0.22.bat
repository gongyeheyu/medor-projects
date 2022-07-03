@echo off
if exist "%SystemRoot%\SysWOW64" path %path%;%windir%\SysNative;%SystemRoot%\SysWOW64;%~dp0
bcdedit >nul
if '%errorlevel%' NEQ '0' (goto UACPrompt) else (goto UACAdmin)
:UACPrompt
%1 start "" mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&exit
exit /B
:UACAdmin
cd /d "%~dp0"
echo 当前运行路径是：%CD%
echo 已获取管理员权限
@echo off
Title JI'OS 21
:h
cls
Echo 0.退出
Echo 1.桌面
Echo 2.应用程序
Set /p a=请输入数字来执行你的操作
If %a%==0 goto 0
If %a%==1 goto 1
If %a%==2 goto 3
Echo 输入错误，请重新输入！
Ping /n 2 127.0.0.1 >nul
Goto h
:0
Cls
Echo 感谢使用，再见！
Ping /n 2 127.0.0.1 >nul
Exit
:1
cls                                                                                             
echo $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ji desktop$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
echo $                                                0.返回
echo $                                             1.应用程序 
echo $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Set /p d=请输入数字来执行你的操作
If %d%==0 goto h
If %d%==1 goto 3
Cls
Echo 输入错误，请重新输入！
Ping /n 2 127.0.0.1 >nul
Goto 1
:3
Cls
Echo 1.IP地址查询
Echo 2.软件查询
Echo 3.本地连接
Echo 4.清理垃圾
Echo 5.写入文档
echo 6.Windows修复
Echo 7.主页
echo 8.桌面
echo 9.关于
echo 10.WLAN热点
Set /p @=请输入数字来执行你的操作
If %@%==1 goto @1
If %@%==2 goto @2
If %@%==3 goto #3
If %@%==4 goto #1
If %@%==5 goto #2
If %@%==6 goto wx
If %@%==7 goto h
If %@%==8 goto 1
If %@%==9 goto ab
If %@%==10 goto $
Cls
Echo 输入错误，请重新输入！
Ping /n 2 127.0.0.1 >nul
Goto 3
:@1
Cls
Ipconfig/all
Echo 按下任意键回到菜单
Pause>nul
Cls
Goto 3
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
cls
goto 3
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
Goto 3
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
Goto 1
:#2.3.1 
Cls
Echo 正在启用本地连接…
Netsh interface set interface name=”以太网” admin=ENABLED
Ping /n 2 127.0.0.1 >nul
Goto 3
:ab
cls
echo JIOS工具箱 版权没有 2020 2021 2022
echo 版本0.22
echo 当前运行路径是：%CD%
echo 0.返回
Set /p abo=请输入数字来执行你的操作
If %abo%==0 goto 3
If %abo%==jios21 goto cai
Cls
Echo 输入错误，请重新输入！
Ping /n 2 127.0.0.1 >nul
Goto ab
:cai
cls
echo         j   i i i i i  ' o o o o o   s s s s s      2 2 2 2 2     1     
echo         j       i        o       o   s                      2    11
echo         j       i        o       o   s s s s s      2 2 2 2 2     1
echo         j       i        o       o           s      2             1
echo j j j j j   i i i i i    o o o o o   s s s s s      2 2 2 2 2   11111   
echo _______________
echo 编写：rooson
pause
goto ab
:wx
cls
sfc /scannow
pause
goto 3
:$
@ECHO off
:$start
CLS
COLOR 3f
MODE con: COLS=42 LINES=28
ECHO.
ECHO    ┏━━━━━━━━━━━━━━━┓

ECHO    ┃请选择要进行的操作，然后按回车┃

ECHO    ┗━━━━━━━━━━━━━━━┛

ECHO.

ECHO               1. 开启热点

ECHO               ──────

ECHO               2. 发射信号

ECHO               ──────

ECHO               3. 关闭信号

ECHO               ──────

ECHO               4. 关闭热点

ECHO               ──────

ECHO               5. 重置密码

ECHO               ──────

ECHO               6. 重置名称

ECHO               ──────

ECHO               7. 网络信息

ECHO               ──────

ECHO               8. 使用帮助

ECHO               ──────

ECHO               9. 懒人设置

ECHO               ──────

ECHO               0. 退出程序

ECHO               ──────
:ch
SET Choice=
SET /P Choice=选择操作并回车:
IF NOT "%Choice%"=="" SET Choice=%Choice:~0,1%
ECHO.
IF /I "%Choice%"=="1" GOTO $1
IF /I "%Choice%"=="2" GOTO $2
IF /I "%Choice%"=="3" GOTO $3
IF /I "%Choice%"=="4" GOTO $4
IF /I "%Choice%"=="5" GOTO $5
IF /I "%Choice%"=="6" GOTO $6
IF /I "%Choice%"=="7" GOTO $7
IF /I "%Choice%"=="8" GOTO $8
IF /I "%Choice%"=="9" GOTO $moren
IF /I "%Choice%"=="0" GOTO e4nd

ECHO 选择无效，请重新输入

ECHO.
GOTO ch
:$1
:: 开启热点
CLS
COLOR 3f
MODE con: COLS=50 LINES=25
ECHO.

ECHO               ┏━━━━━━━━━┓

ECHO               ┃  继续设置请按 1  ┃

ECHO               ┃  返回菜单请按 2  ┃

ECHO               ┗━━━━━━━━━┛

Set /p ask=选择:

ECHO.
if /i "%ask%"=="1" goto $SHE
if /i "%ask%"=="2" goto $start
:$SHE

ECHO.

netsh wlan set hostednetwork mode=allow

ECHO.

ECHO                 ┏━━━━━━━━┓

ECHO                 ┃ 请设置热点名称 ┃

ECHO                 ┗━━━━━━━━┛

ECHO.

set /p Ming=请设置名称：

netsh wlan set hostednetwork ssid=%Ming%

ECHO.

ECHO                 ┏━━━━━━━━┓

ECHO                 ┃ 请设置热点密码 ┃

ECHO                 ┗━━━━━━━━┛

ECHO.

set /p Mima=请设置8位以上的密码：

netsh wlan set hostednetwork key=%Mima%

::是否发射信号
CLS
COLOR 3f
MODE con: COLS=41 LINES=22
ECHO.

ECHO      ┏━━━━━━━━━━━━━┓

ECHO      ┃   您现在是否要发射信号   ┃ 

ECHO      ┃       确认请按 1         ┃   

ECHO      ┃ 暂时不发射请按 2 返回菜单┃

ECHO      ┗━━━━━━━━━━━━━┛

ECHO.

Set /p ask=选择:

ECHO.

if /i "%ask%"=="1" goto $2
if /i "%ask%"=="2" goto $start
:$2
::发射信号
CLS
COLOR 3f
MODE con: COLS=41 LINES=22
netsh wlan start hostednetwork

ECHO.

ECHO      ┏━━━━━━━━━━━━━┓

ECHO      ┃ 已发射信号，按任意键返回 ┃

ECHO      ┗━━━━━━━━━━━━━┛

ECHO.

PAUSE >NUL
GOTO start
:$3
::关闭信号
CLS
netsh wlan stop hostednetwork
ECHO.

ECHO     ┏━━━━━━━━━━━━━━━┓

ECHO     ┃ 已关闭发射信号，按任意键返回 ┃

ECHO     ┗━━━━━━━━━━━━━━━┛

ECHO.

PAUSE >NUL

GOTO start
:$4
::关闭热点
CLS
netsh wlan set hostednetwork mode=disallow

ECHO.

ECHO      ┏━━━━━━━━━━━━━━┓

ECHO      ┃ 已关闭热点，请按任意键返回 ┃

ECHO      ┗━━━━━━━━━━━━━━┛

ECHO.

PAUSE >NUL

GOTO $start
:$5
:: 重置密码
CLS
ECHO.

ECHO          ┏━━━━━━━━┓

ECHO          ┃ 请重置热点密码 ┃

ECHO          ┗━━━━━━━━┛

ECHO.

set /p ChongMi=请重置8位以上的密码：

netsh wlan set hostednetwork key=%ChongMi%

ECHO.

ECHO    ┏━━━━━━━━━━━━━━━━┓

ECHO    ┃ 已重置热点密码，请按任意键返回 ┃

ECHO    ┗━━━━━━━━━━━━━━━━┛

ECHO.

PAUSE >NUL

GOTO $start
:$6
:: 重置名称
CLS

ECHO.

ECHO          ┏━━━━━━━━┓

ECHO          ┃ 请重置热点名称 ┃

ECHO          ┗━━━━━━━━┛

ECHO.

set /p ZhongMing=请设置名称：

netsh wlan set hostednetwork ssid=%ZhongMing% 

netsh wlan start hostednetwork

ECHO.

ECHO    ┏━━━━━━━━━━━━━━━━┓

ECHO    ┃ 已重置热点名称，请按任意键返回 ┃

ECHO    ┗━━━━━━━━━━━━━━━━┛

ECHO.

PAUSE >NUL
GOTO $start
:$7
::网络信息显示
CLS
COLOR 3f
MODE con: COLS=47 LINES=26
ECHO.

ECHO               ┏━━━━━━━━┓

ECHO               ┃  网络信息显示  ┃

ECHO               ┗━━━━━━━━┛

ECHO.

netsh wlan show hostednetwork

ECHO -----------------------

ECHO.

PAUSE

GOTO $start

:$moren
cls
::如果你不想每次都进入第一步设置名称密码等，可以用自己设置好的，以下参数可以自
己改
::修改以下两行即可，两行其中ssid为热点名称；key为密码
set ssid=jios-wlan
set /a key=jios-wlan
netsh wlan set hostednetwork mode=allow ssid=%ssid% key=%key%
ECHO.

ECHO.

ECHO.

ECHO ━━━━━━━━━━━━━━━━━━━━

ECHO  热点默认名称为: %ssid%         

ECHO  热点默认密码为: %key%     

ECHO ━━━━━━━━━━━━━━━━━━━━

ECHO.

netsh wlan start hostednetwork
pause
goto $start
:$8
::使用说明
CLS
COLOR 3f
MODE con: COLS=69 LINES=33
ECHO.

ECHO                     ┏━━━━━━━━━━━━┓

ECHO                     ┃    使   用   说   明   ┃

ECHO                     ┗━━━━━━━━━━━━┛

ECHO.

ECHO  -------------------------------------------------------------------

ECHO   1.使用此程序前请设置好计算机网络共享！此程序在windows10系统下测试

ECHO     可用。电脑需配置有无线网卡，并支持承载网络，否则无法使用本程序

ECHO  -------------------------------------------------------------------

ECHO   2.每次使用都需要设置第1或第9步，为热点设置名称和密码，并发射即可！

ECHO  -------------------------------------------------------------------

ECHO   3.名称建议用字母和数字，请尽量不用复杂的符号，否则系统可能不识别

ECHO  -------------------------------------------------------------------

ECHO   4.密码请设置8位数以上，请尽量不用复杂的符号， 否则系统可能不识别

ECHO  -------------------------------------------------------------------

ECHO   5.若出现搜索到信号但是连接不了或上不了网的情况，那么重新设置第1步

ECHO  -------------------------------------------------------------------

ECHO   6.第3、4步区别：第3步为“已停止承载网络”，若进入信息显示会看到

ECHO     “承载网络状态”为未启用；第4步为“承载网络模式已设置为禁止”

ECHO     进入信息显示会看到“承载网络状态”为不可用。不用热点的时候选择

ECHO     第3或第4步都可。若之后想继续使用无线发射，需再次设置第1或第9步

ECHO  -------------------------------------------------------------------

ECHO   7.如果不想每次进入第1步设置名称和密码，则可以进入第9步，一键设置

ECHO     即可发射热点。默认名称为WIFI，密码为1234567890；若想更改默认名

ECHO     称及密码，可进入代码中的:moren修改其中两行即可（代码有修改说明）

ECHO  -------------------------------------------------------------------

ECHO   8.计算机关机也会自动关闭无线热点，故启动电脑后若想使用无线发射，

ECHO     需再次设置第1步。如需要更改密码或名称，可在主菜单选择第5步或第

ECHO     6步进行更改，然后在接收设备上重新连接即可。

ECHO  -------------------------------------------------------------------

ECHO.

ECHO 请按任意键返回主菜单...
PAUSE >NUL
GOTO $start
:$end
Exit