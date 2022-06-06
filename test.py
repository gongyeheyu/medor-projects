print('计算器')
i = input(']')
i = i.split(' ')
a = int(i[0])
b = i[1]
c = int(i[2])
if b == '+':
    print(a+c)
elif b == '-':
    print(a-c)
elif b == '*':
    print(a*c)
elif b == '/':
    print(a/c)
elif b == '%':
    print(a%c)
elif b == '**':
    print(a**c)
elif b == '//':
    print(a//c)

