@echo off
if exist "%SystemRoot%\SysWOW64" path %path%;%windir%\SysNative;%SystemRoot%\SysWOW64;%~dp0
bcdedit >nul
if '%errorlevel%' NEQ '0' (goto UACPrompt) else (goto UACAdmin)
:UACPrompt
%1 start "" mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&exit
exit /B
:UACAdmin
cd /d "%~dp0"
echo ��ǰ����·���ǣ�%CD%
echo �ѻ�ȡ����ԱȨ��
@echo off
Title JI'OS 21
:h
cls
Echo 0.�˳�
Echo 1.����
Echo 2.Ӧ�ó���
Set /p a=������������ִ����Ĳ���
If %a%==0 goto 0
If %a%==1 goto 1
If %a%==2 goto 3
Echo ����������������룡
Ping /n 2 127.0.0.1 >nul
Goto h
:0
Cls
Echo ��лʹ�ã��ټ���
Ping /n 2 127.0.0.1 >nul
Exit
:1
cls                                                                                             
echo $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ji desktop$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
echo $                                                0.����
echo $                                             1.Ӧ�ó��� 
echo $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Set /p d=������������ִ����Ĳ���
If %d%==0 goto h
If %d%==1 goto 3
Cls
Echo ����������������룡
Ping /n 2 127.0.0.1 >nul
Goto 1
:3
Cls
Echo 1.IP��ַ��ѯ
Echo 2.�����ѯ
Echo 3.��������
Echo 4.��������
Echo 5.д���ĵ�
echo 6.Windows�޸�
Echo 7.��ҳ
echo 8.����
echo 9.����
echo 10.WLAN�ȵ�
Set /p @=������������ִ����Ĳ���
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
Echo ����������������룡
Ping /n 2 127.0.0.1 >nul
Goto 3
:@1
Cls
Ipconfig/all
Echo ����������ص��˵�
Pause>nul
Cls
Goto 3
:@2
Cls
Echo ������Ŀ¼�������
Set /p @2.1=��[c d e f����]
Set /p @2.2=��һĿ¼
Set /p @2.3=��һĿ¼
Set /p @2.4=��һĿ¼
Set /p @2.5=��һĿ¼
Set /p @2.6=��һĿ¼
Set /p @2.7=��һĿ¼
Set /p @2.8=��һĿ¼
Set /p @2.9=��һĿ¼
Set /p @2.10=��һĿ¼
Set /p @2.11=��һĿ¼
:@2start 
Start ��:%@2.1%\%@2.2%\%@2.3%\%@2.4%\%@2.5%\%@2.6%\%@2.7%\%@2.8%\%@2.9%\%@2.10%\%@2.11%��
cls
goto 3
:#1
Cls
Echo ׼������ϵͳ������.
Ping /n 3 127.0.0.1 >nul
Del /f /s /q %systemdrive%\*.tmp&del /f /s /q %systemdrive%\*._mp 
Del /f /s /q %systemdrive%\*.log&del /f /s /q %systemdrive%\*.gid 
Del /f /s /q %systemdrive%\*.chk&del /f /s /q %systemdrive%\*.old 
Del /f /s /q %systemdrive%\recycled\*.*&del /f /s /q %windir%\*.bak 
Del /f /s /q %windir%\prefetch\*.*&rd /s /q %windir%\temp & md %windir%\temp 
Del /f /q %userprofile%\cookies\*.*&del /f /q %userprofile%\recent\*.* 
Del /f /s /q ��%userprofile%\Local Settings\Temporary Internet Files\*.*�� 
Del /f /s /q ��%userprofile%\Local Settings\Temp\*.*��
Del /f /s /q ��%userprofile%\recent\*.*�� 
Cls
Echo �������!
Ping /n 2 127.0.0.1 >nul
Goto 3
:#2
Echo �������ļ���
Set /p biaoti=
Echo �������׺��
Set /p houzhui=
Echo ������ɣ�
Echo ���������ʼ�����ı�
Pause>nul
Cls
Echo ����������ok�Ա��������
Goto #2.2.1
:#2.2.1
Set /p batdazi=
If ��%batdazi%��==��ok�� goto !
Echo ----------------------- >>%biaoti%.%houzhui%
Echo %batdazi%>>%biaoti%.%houzhui%
Goto #2.2.1
:#3
Cls
Echo 1.��������/����
Echo 2.��������/�ر�
Set /p KEY=������������ִ����Ĳ���
If %KEY% == 1 goto #2.3.1
If %KEY% == 2 goto #2.3.2
Cls
Echo ����������������룡
Ping /n 2 127.0.0.1 >nul
Goto #3
:#2.3.2
Cls
Echo �Ѿ����ñ������ӡ�
Netsh interface set interface name=����̫���� admin=DISABLED
Ping /n 2 127.0.0.1 >nul
Goto 1
:#2.3.1 
Cls
Echo �������ñ������ӡ�
Netsh interface set interface name=����̫���� admin=ENABLED
Ping /n 2 127.0.0.1 >nul
Goto 3
:ab
cls
echo JIOS������ ��Ȩû�� 2020 2021 2022
echo �汾0.22
echo ��ǰ����·���ǣ�%CD%
echo 0.����
Set /p abo=������������ִ����Ĳ���
If %abo%==0 goto 3
If %abo%==jios21 goto cai
Cls
Echo ����������������룡
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
echo ��д��rooson
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
ECHO    ����������������������������������

ECHO    ����ѡ��Ҫ���еĲ�����Ȼ�󰴻س���

ECHO    ����������������������������������

ECHO.

ECHO               1. �����ȵ�

ECHO               ������������

ECHO               2. �����ź�

ECHO               ������������

ECHO               3. �ر��ź�

ECHO               ������������

ECHO               4. �ر��ȵ�

ECHO               ������������

ECHO               5. ��������

ECHO               ������������

ECHO               6. ��������

ECHO               ������������

ECHO               7. ������Ϣ

ECHO               ������������

ECHO               8. ʹ�ð���

ECHO               ������������

ECHO               9. ��������

ECHO               ������������

ECHO               0. �˳�����

ECHO               ������������
:ch
SET Choice=
SET /P Choice=ѡ��������س�:
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

ECHO ѡ����Ч������������

ECHO.
GOTO ch
:$1
:: �����ȵ�
CLS
COLOR 3f
MODE con: COLS=50 LINES=25
ECHO.

ECHO               ����������������������

ECHO               ��  ���������밴 1  ��

ECHO               ��  ���ز˵��밴 2  ��

ECHO               ����������������������

Set /p ask=ѡ��:

ECHO.
if /i "%ask%"=="1" goto $SHE
if /i "%ask%"=="2" goto $start
:$SHE

ECHO.

netsh wlan set hostednetwork mode=allow

ECHO.

ECHO                 ��������������������

ECHO                 �� �������ȵ����� ��

ECHO                 ��������������������

ECHO.

set /p Ming=���������ƣ�

netsh wlan set hostednetwork ssid=%Ming%

ECHO.

ECHO                 ��������������������

ECHO                 �� �������ȵ����� ��

ECHO                 ��������������������

ECHO.

set /p Mima=������8λ���ϵ����룺

netsh wlan set hostednetwork key=%Mima%

::�Ƿ����ź�
CLS
COLOR 3f
MODE con: COLS=41 LINES=22
ECHO.

ECHO      ������������������������������

ECHO      ��   �������Ƿ�Ҫ�����ź�   �� 

ECHO      ��       ȷ���밴 1         ��   

ECHO      �� ��ʱ�������밴 2 ���ز˵���

ECHO      ������������������������������

ECHO.

Set /p ask=ѡ��:

ECHO.

if /i "%ask%"=="1" goto $2
if /i "%ask%"=="2" goto $start
:$2
::�����ź�
CLS
COLOR 3f
MODE con: COLS=41 LINES=22
netsh wlan start hostednetwork

ECHO.

ECHO      ������������������������������

ECHO      �� �ѷ����źţ������������ ��

ECHO      ������������������������������

ECHO.

PAUSE >NUL
GOTO start
:$3
::�ر��ź�
CLS
netsh wlan stop hostednetwork
ECHO.

ECHO     ����������������������������������

ECHO     �� �ѹرշ����źţ������������ ��

ECHO     ����������������������������������

ECHO.

PAUSE >NUL

GOTO start
:$4
::�ر��ȵ�
CLS
netsh wlan set hostednetwork mode=disallow

ECHO.

ECHO      ��������������������������������

ECHO      �� �ѹر��ȵ㣬�밴��������� ��

ECHO      ��������������������������������

ECHO.

PAUSE >NUL

GOTO $start
:$5
:: ��������
CLS
ECHO.

ECHO          ��������������������

ECHO          �� �������ȵ����� ��

ECHO          ��������������������

ECHO.

set /p ChongMi=������8λ���ϵ����룺

netsh wlan set hostednetwork key=%ChongMi%

ECHO.

ECHO    ������������������������������������

ECHO    �� �������ȵ����룬�밴��������� ��

ECHO    ������������������������������������

ECHO.

PAUSE >NUL

GOTO $start
:$6
:: ��������
CLS

ECHO.

ECHO          ��������������������

ECHO          �� �������ȵ����� ��

ECHO          ��������������������

ECHO.

set /p ZhongMing=���������ƣ�

netsh wlan set hostednetwork ssid=%ZhongMing% 

netsh wlan start hostednetwork

ECHO.

ECHO    ������������������������������������

ECHO    �� �������ȵ����ƣ��밴��������� ��

ECHO    ������������������������������������

ECHO.

PAUSE >NUL
GOTO $start
:$7
::������Ϣ��ʾ
CLS
COLOR 3f
MODE con: COLS=47 LINES=26
ECHO.

ECHO               ��������������������

ECHO               ��  ������Ϣ��ʾ  ��

ECHO               ��������������������

ECHO.

netsh wlan show hostednetwork

ECHO -----------------------

ECHO.

PAUSE

GOTO $start

:$moren
cls
::����㲻��ÿ�ζ������һ��������������ȣ��������Լ����úõģ����²���������
����
::�޸��������м��ɣ���������ssidΪ�ȵ����ƣ�keyΪ����
set ssid=jios-wlan
set /a key=jios-wlan
netsh wlan set hostednetwork mode=allow ssid=%ssid% key=%key%
ECHO.

ECHO.

ECHO.

ECHO ����������������������������������������

ECHO  �ȵ�Ĭ������Ϊ: %ssid%         

ECHO  �ȵ�Ĭ������Ϊ: %key%     

ECHO ����������������������������������������

ECHO.

netsh wlan start hostednetwork
pause
goto $start
:$8
::ʹ��˵��
CLS
COLOR 3f
MODE con: COLS=69 LINES=33
ECHO.

ECHO                     ����������������������������

ECHO                     ��    ʹ   ��   ˵   ��   ��

ECHO                     ����������������������������

ECHO.

ECHO  -------------------------------------------------------------------

ECHO   1.ʹ�ô˳���ǰ�����úü�������繲���˳�����windows10ϵͳ�²���

ECHO     ���á�������������������������֧�ֳ������磬�����޷�ʹ�ñ�����

ECHO  -------------------------------------------------------------------

ECHO   2.ÿ��ʹ�ö���Ҫ���õ�1���9����Ϊ�ȵ��������ƺ����룬�����伴�ɣ�

ECHO  -------------------------------------------------------------------

ECHO   3.���ƽ�������ĸ�����֣��뾡�����ø��ӵķ��ţ�����ϵͳ���ܲ�ʶ��

ECHO  -------------------------------------------------------------------

ECHO   4.����������8λ�����ϣ��뾡�����ø��ӵķ��ţ� ����ϵͳ���ܲ�ʶ��

ECHO  -------------------------------------------------------------------

ECHO   5.�������������źŵ������Ӳ��˻��ϲ��������������ô�������õ�1��

ECHO  -------------------------------------------------------------------

ECHO   6.��3��4�����𣺵�3��Ϊ����ֹͣ�������硱����������Ϣ��ʾ�ῴ��

ECHO     ����������״̬��Ϊδ���ã���4��Ϊ����������ģʽ������Ϊ��ֹ��

ECHO     ������Ϣ��ʾ�ῴ������������״̬��Ϊ�����á������ȵ��ʱ��ѡ��

ECHO     ��3���4�����ɡ���֮�������ʹ�����߷��䣬���ٴ����õ�1���9��

ECHO  -------------------------------------------------------------------

ECHO   7.�������ÿ�ν����1���������ƺ����룬����Խ����9����һ������

ECHO     ���ɷ����ȵ㡣Ĭ������ΪWIFI������Ϊ1234567890���������Ĭ����

ECHO     �Ƽ����룬�ɽ�������е�:moren�޸��������м��ɣ��������޸�˵����

ECHO  -------------------------------------------------------------------

ECHO   8.������ػ�Ҳ���Զ��ر������ȵ㣬���������Ժ�����ʹ�����߷��䣬

ECHO     ���ٴ����õ�1��������Ҫ������������ƣ��������˵�ѡ���5�����

ECHO     6�����и��ģ�Ȼ���ڽ����豸���������Ӽ��ɡ�

ECHO  -------------------------------------------------------------------

ECHO.

ECHO �밴������������˵�...
PAUSE >NUL
GOTO $start
:$end
Exit