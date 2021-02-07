"""
用于分解正数的质因子
"""


#分解出一个因子
def fact(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return i, n//i
    return True #确实是质数

#得到输入
n = int(input('A number is needed:'))
print(f'{n}=',end='')
factors = list()

while True:
    #分解为质数时停止
    if fact(n)==True:
        factors.append(n)
        break
    a,b = fact(n)
    factors.append(a)
    n = b

#输出
print("*".join([str(i) for i in factors]))

