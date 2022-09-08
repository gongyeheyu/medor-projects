# -*- coding: utf-8 -*-
#这个我是想做一个差量备份的，但是一直没完成

ver = '22.9'
mainame = 'medor-backup'
mainpath = '\AppData\Roaming\medor\backup'
import py7zr
with py7zr.SevenZipFile("target.7z", 'w') as archive:
    archive.writeall("lib")