# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

# Resolução do professor

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificando o menor valor
if a < b and a < c:
    menor = a
    print(f'O primeiro valor {a} é o menor.')
if b < a and b < c:
    menor = b
    print(f'O segundo valor {b} é o menor.')
if c < a and c < b:
    menor = b
    print(f'O terceiro valor {c} é o menor.')

# Verificando o maior valor
if a > b and a > c:
    maior = a
    print(f'O primeiro valor {a} é o maior.')
if b > a and b > c:
    maior = b
    print(f'O segundo valor {b} é o maior.')
if c > a and c > b:
    maior = c
    print(f'O terceiro valor {c} é o maior.')


# Outra forma de resolver, diminuindo um if
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

# Verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor valor digitado foi {menor}')

# Verificando o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor digitado foi {maior}')

   




