# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido.

# com nomes definidos
import random
aluno1 = 'João'
aluno2 = 'Ana'
aluno3 = 'Paula'
aluno4 = 'André'
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi: {escolhido}')


# com nomes aleatórios
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Dgite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi: {escolhido}')
