# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
numero = random.randint(0,5)
palpite = int(input('Digite um número e tente acertar o número que pensei: '))
if palpite == numero:
    print(f'O número que pensei foi {numero} e você pensou: {palpite}. PARABÉNS VOCÊ VENCEU')
else:
    print(f'O número que pensei foi {numero} e você pensou {palpite}, VOCÊ PERDEU!!')

