#生成字典a-z
import string
import random
a=string.ascii_lowercase
#生成字典0-9
b=string.digits
#生成字典A-Z
c=string.ascii_uppercase
#生成字典符号
d=string.punctuation
#生成字典所有
f=a+b+c+d
#输入需要生成的密码长度
n=int(input('请输入需要生成的密码长度：'))
#生成密码
p=''
for i in range(n):
    p+=f[random.randint(0,len(f)-1)]
#输出密码
print('生成的密码为：',p)
#输出密码长度
print('生成的密码长度为：',len(p))
