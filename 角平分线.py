k1 = int(input('请输入k1:'))
k2 = int(input('请输入k2:'))
x1 = (1 + k2 ** 2) ** 0.5
x2 = (1 + k1 ** 2) ** 0.5
k = -1 /( (k1 * x1 - k2 * x2)/(x1 - x2))
print('k值为', k)
