# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'

cidade = str(input('Digite o nome de uma cidade: ')).strip() #quando tivermos uma string onde o usuário irá digitar algo, usamos o strip para eliminarmos qualquer espaço digitado
print(cidade[:5].upper() == 'SANTO')
