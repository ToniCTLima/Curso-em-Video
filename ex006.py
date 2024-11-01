# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n**(1/2)
print('O dobro de {} é: {}'.format(n, dobro))
print('O triplo de {} é: {}'.format(n, triplo))
print('A raiz quadrada de {} é: {:.2f}'.format(n, raiz))

# Outra forma do código com menos variáveis

n = int(input('Digite um número: '))
print(f'O dobro de {n} é:',n*2, 'O triplo é:',n*3, 'e a raiz quadrada é:',round(n**(1/2)))