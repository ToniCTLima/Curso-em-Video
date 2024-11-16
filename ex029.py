# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada km acima do limite.

# VELOCIDADE
import random
velo = random.randint(70,100)
excesso_velo = velo - 80
multa = excesso_velo * 7

# MULTA
print(velo)
if velo > 80:
    print(f'Você foi multado, sua velocidade era de {velo} km/h. O limite é de 80 km/h.')
    print(f'O valor da multa é de R$ {multa}')
else:
    print('Você está dentro dos limites de velocidade.')

# Solução do Professor

velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R$ {:.2f}'.format(multa))

print('Tenha um bom dia! Dirija com segurança.')
