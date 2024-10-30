# Crie um programa que leia dois números e mostre a soma entre eles

n1 = int(input('Digite um número: ')) # int mostra somente números inteiros, não possuem parte decimal. então se o usuário digitar: 1.222 o programa irá apresentar erro.
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print('A soma de {} mais {} é igual a: {}'.format(n1, n2, soma))
