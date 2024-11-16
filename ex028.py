# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
numero = random.randint(0,5)
palpite = int(input('Digite um número e tente acertar o número que pensei: '))
if palpite == numero:
    print(f'O número que pensei foi {numero} e você pensou: {palpite}. PARABÉNS VOCÊ VENCEU')
else:
    print(f'O número que pensei foi {numero} e você pensou {palpite}, VOCÊ PERDEU!!')

# Solução do professor

from random import randint
from time import sleep # faz o computador esperar por um tempo determinado, comando na linha 20
computador = randint(0,5) # Faz o computador sortear um número entre 0 e 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar.')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))


