#这东西是想做一个模拟股票交易的

import random
import time
print('loading')
money = 100
#每秒money增加1
money = money + 1
print(money)
time.sleep(1)

def gu(stock,stock_price,stock_num,price_change):
    #随机生成三个股票
    stock = ['股票A','股票B','股票C']
    #随机生成三个股票价格
    pricea = random.randint(1,100)
    priceb = random.randint(1,100)
    pricec = random.randint(1,100)
    stock_price = [pricea,priceb,pricec]
    #随机生成三个股票数量
    numa = random.randint(1,100)
    numb = random.randint(1,100)
    numc = random.randint(1,100)
    stock_num = [numa,numb,numc]
    #价格每秒随机增减
    pca = random.randint(-1,1)
    pcb = random.randint(-1,1)
    pcc = random.randint(-1,1)
    price_change = [pca,pcb,pcc]
    #股票数量每秒随机增减
    num_change = [random.randint(-1,1),random.randint(-1,1),random.randint(-1,1)]
    return stock,stock_price,stock_num,price_change,num_change

#买入股票
def buy():
    #输入股票名称
    buy_stock = input('输入股票名称：')
    #输入股票数量
    buy_num = input('输入买入数量：')
    #扣除money
    money = money - buy_num
    #输出
    print('买入了' + buy_stock + '，数量' + buy_num + '，剩余' + str(money))
    

#开始
def st():
    stock_price = gu(stock_price)
    stock_num = gu(stock_num)
    price_change = gu(price_change)
    num_change = gu(num_change)
    print('欢迎来到股票交易系统')
    print('股票    价格    数量    涨跌    涨跌幅')
    print('A' + ' ' + str(stock_price[0]) + ' ' + str(stock_num[0]) + ' ' + str(price_change[0]) + ' ' + str(price_change[0]/stock_price[0]))
    print('B' + ' ' + str(stock_price[1]) + ' ' + str(stock_num[1]) + ' ' + str(price_change[1]) + ' ' + str(price_change[1]/stock_price[1]))
    print('C' + ' ' + str(stock_price[2]) + ' ' + str(stock_num[2]) + ' ' + str(price_change[2]) + ' ' + str(price_change[2]/stock_price[2]))
    print('您的资金为' + str(money))
    #每秒刷新一次
    time.sleep(1)
    st()
st()