# Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas, o nome com todas as letras minúsculas, quantas letras ao todo(sem contar espaços), quantas letras tem o primeiro nome.

nome = str(input(('Digite seu nome completo: '))).strip() # usando a finção strip, eliminamos qualquer espação indevido que o usuário possa digitar
print(f'Seu nome com todas as letras maiúsculas fica: {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas fica: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)-nome.count(' ')} letras')
print(f'Seu primeiro nome têm {nome.find(' ')} ')