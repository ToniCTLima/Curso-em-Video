# Crie um programa que leia o comprimento do cateto adjacente e do cateto oposto de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

# sem importar math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir: {:.2f}'.format(hi))
print(f'A hipotenusa vai medir {hi:.2f}')

# importando math
import math
co = float(input('Comprimento do cateo oposto:'))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir: {hi:.2f}')
