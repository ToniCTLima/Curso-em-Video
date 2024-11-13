# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.

num = float(input('Digite um número: '))
print(f'O número digitado {num}, tem sua parte inteira: {int(num)}')

# importando de math

import math
num = float(input('Digite um número: '))
int = math.trunc(num)
print(f'O número digitado {num}, têm a parte inteira {int}')

# importando somente trunc from math

from math import trunc
num = float(input('Digite um número: '))
int = trunc(num)
print(f'O valor digitado foi {num} e sua porção inteira é {int}')
