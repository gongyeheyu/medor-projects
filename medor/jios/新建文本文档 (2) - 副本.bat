@echo off
Title ����̫��
Cls
systeminfo
cls
Echo 0.�˳�
Echo 1.��Դ
Echo 2.��ݲ�ѯ
Echo 3.С����
Set /p a=������������ִ����Ĳ���
If %a%==0 goto 0
If %a%==1 goto 1
If %a%==2 goto 2
If %a%==3 goto 3
Echo ����������������룡
Ping /n 2 127.0.0.1 >nul
Goto !
:0
Cls
Echo ��лʹ�ã��ټ���
Ping /n 2 127.0.0.1 >nul
Exit
:1
Cls
Echo 1.�ػ�
Echo 2.����
Echo 3.����
Echo 4.ע��
Echo 5.���ز˵�
Set /p !=������������ִ����Ĳ���
If %!%==1 goto !1
If %!%==2 goto !2
If %!%==3 goto !3
If %!%==4 goto !4
If %!%==5 goto !5
Cls
Echo ����������������룡
Ping /n 2 127.0.0.1 >nul
Goto 1
:!1
Shutdown -s -f -t 30
Cls
Echo �Ƿ���ֹ�������ֹ�ػ�������a �����Ҫֱ�ӹػ�������b
Set /p C=��������ĸ��ִ����Ĳ���
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
Echo 1.IP��ַ��ѯ
Echo 2.�����ѯ
Echo 3.δ����
Echo 4.���ز˵�
Set /p @=������������ִ����Ĳ���
Cls
If %@%==1 goto @1
If %@%==2 goto @2
If %@%==4 goto @4
Cls
Echo ����������������룡
Ping /n 2 127.0.0.1 >nul
Goto 2
:@1
Cls
Ipconfig/all
Echo ����������ص��˵�
Pause>nul
Cls
Goto !
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
:@4
Cls
Goto !
:3
Cls
Echo 1.��������
Echo 2.д���ĵ�
Echo 3.��������
Set /p #=������������ִ����Ĳ���
If %#%==1 goto #1
If %#%==2 goto #2
If %#%==3 goto #3
Cls
Echo ����������������룡
Ping /n 2 127.0.0.1 >nul
Goto 3
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
Goto !
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
Goto !
:#2.3.1 
Cls
Echo �������ñ������ӡ�
Netsh interface set interface name=����̫���� admin=ENABLED
Ping /n 2 127.0.0.1 >nul
Goto !