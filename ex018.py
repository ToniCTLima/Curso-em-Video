# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite um ângulo: ')) # devemos converter o ângulo para radiano
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'O seno do ângulo {ang} é {seno:.2f}')
print(f'O cosseno do ângulo {ang} é {coss:.2f}')
print(f'A tangente do ângulo {ang} é {tang:.2f}')
