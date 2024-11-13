# Faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada.

import random
aluno1 = 'Ana'
aluno2 = 'Lara'
aluno3 = 'Toni'
aluno4 = 'Lucas'
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'A ordem de sorteio é: {lista}')
