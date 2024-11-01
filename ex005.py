# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
antecessor = n - 1
sucessor = n + 1
print('O número digitado foi: {}. Seu antecessor é: {} e seu sucessor é: {}'.format(n, antecessor, sucessor))
