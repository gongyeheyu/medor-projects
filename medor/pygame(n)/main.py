#这个我是想用pygame做一个类似于galgame的游戏的，废掉了

import random,sys,os
def p0():
    print('''
    夏旭东的夏天并不是非常好
    高中没有达到分数线，不过至少能上，但他已经不在意这些了
    找个归属，找个归属，这就是他想做的
    01 与父母聊聊
    02 自己查查升学相关''') #(隐藏结局：熬夜上网触电休克)
    i = input(':')
    if i == '01':
        p01()
    elif i == '02':
        p02()
    else:
        print('重新输入')
        input()
        p0()

def p01():
    def p01_1():
        print('''
        天气不算好，雨浇的离谱，父亲没成功去上班，就请假了
        011 与父亲交谈
        012 与母亲交谈''')
        i = input(':')
        if i == '01':
            p011()
        elif i == '02':
            p012()
        else:
            print('重新输入')
            back(3)
    def p01_2():
        print('''
        天气好的很，妈妈是偷懒没去上班，你决定跟她聊聊
        012 与母亲交谈''')
        i = input(':')
        if i == '01':
            p012()
        else:
            print('重新输入')
            back(3)
    oneor2 = int(random.randint(1,100))
    if oneor2 <= '50':
        p01_1()
    elif oneor2 >= '51':
        p01_2()
    else:
        print('重新输入')
        back(3)

def p02():
    v02 = True
    print('''
    你自己查了全部事宜了，感觉运筹帷幄，于是现在你要
    011 与父亲交谈
    012 与母亲交谈
    013 这是我的时代''')
    i = input(':')
    if i == '011':
        p011()
    elif i == '012':
        p012()
    elif i == '013':
        p013()
    else:
        print('重新输入')
        back(3)

def cls():
    os.system('cls')

def back(where):
    w = sys._getframe(1).f_code.co_name
    #where=0为直接返回主菜单，where=1为询问后返回主菜单#
    #where=2为直接返回上一级菜单,where=3为询问后返回上一级菜单
    if where == 0:
        cls() 
        #apps()
    elif where == 1:
        input("按任意键返回")
        cls()
        #apps()
    elif where == 2:
        cls()
        #调用w中的函数名
        globals()[w]()
    elif where == 3:
        input("按任意键返回")
        cls()
        globals()[w]()
    else:
        print("输入错误")
        back(3)