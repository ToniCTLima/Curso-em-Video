# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra 'A', em que posição ela aparece a primeira vez, em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper() # upper vai jogar toda a frase para maiúscula
print(f'A letra A aparece {frase.count('A')} vezes na frase.') # contando quantas letras 'A' existem na frase
print(f'A letra A aparece pela primeira vez na posição: {frase.find('A')+1}') # colocamos + 1 para iniciarmos a contagem da posição 1 e não da posição 0 que é padrão
print(f'A letra A aparece pela última vez na posição: {frase.rfind('A')+1}')

