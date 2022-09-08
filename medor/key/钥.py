#这个是一个简单的密钥验证

import time
import datetime
#获取现在年月日
def now_time():
    now_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    now_time.split('-')
    return now_time
i = input('请输入密钥')
#16进制转10进制
def split_i(i):
    i_list = i.split('-')
    i_list[0] = int(i_list[0],16)
    i_list[1] = int(i_list[1],16)
    i_list[2] = int(i_list[2],16)
    i_list[3] = int(i_list[3],16)
    i_list[0] = int(i_list[0] / 9)
    i_list[1] = int(i_list[1] / 7)
    i_list[2] = int(i_list[2] / 3)
    i_list[3] = int(i_list[3] / 13)
    print('有效期到' + str(i_list[0]) + '年' + str(i_list[1]) + '月' + str(i_list[2]) + '日')
    #比较现在时间和有效期
    if int(i_list[0]) < int(now_time()[0:4]):
        y = False
    elif int(i_list[0]) >= int(now_time()[0:4]):
        y = True
    if int(i_list[1]) < int(now_time()[5:7]):
        m = False
    elif int(i_list[1]) >= int(now_time()[5:7]):
        m = True
    if int(i_list[2]) < int(now_time()[8:10]):
        d = False
    elif int(i_list[2]) >= int(now_time()[8:10]):
        d = True
    if int(i_list[3]) == int(220412):
        v = True
    else:
        v = False
    if y == True and m == True and d == True and v == True:
        return True
    else:
        return False

if split_i(i):
    print('密钥正确')
else:
    print('密钥错误或已过期')

#GONGYE Heyu 于2022年4月12日完成
#2022 GONGYE Heyu 保留所有权利