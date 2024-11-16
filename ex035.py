# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Solução do professor

s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos informados podem formar um triângulo.')
else:
    print('Os segmentos informados não podem formar um triângulo.')
