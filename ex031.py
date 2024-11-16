# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0.50 por km para viagens até 200 km e R$ 0.45 para viagens mais longas.

km = int(input('Digite a distância em km que vai percorrer: '))
p_200 = km * 0.50
p_201 = km * 0.45
if km <= 200:
    print(f'Você vai viajar {km} km, o valor da sua passagem é R$ {p_200:.2f}')
else:
    print(f'Você vai viajar {km} km, o valor da sua passagem é R$ {p_201:.2f}')

# Resolução do professor

distancia = float(input('Qual é a distância da viagem? '))
print('Você está prestes a começar uma viagem de {:.2f} km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem será de R$ {:.2f}'.format(preco))

# Outra forma de resolver - if simplificado ('operador ternário')

distancia = float(input('Digite a distância da viagem: '))
print('Você está prestes a começar uma viagem de {:.2f} km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.50
print('E o preço da sua passagem será de R$ {:.2f}'.format(preco))



    