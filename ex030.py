# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

numero = int(input('Digite um número para saber se é par ou ímpar: '))
if numero % 2 == 0 :
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')


# Resolução do professor

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))
