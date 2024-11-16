# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250, calcule um aumento de 10%
# Para salários inferiores ou iguais, o aumento é de 15%

sal = float(input('Digite o valor do seu salário: '))
sal_1 = sal + (sal * 10 / 100)
sal_2 = sal + (sal * 15 / 100)
if sal <= 1250:
    print(f'Seu salário de R$ {sal:.2f}, com o aumento de 15% passa a ser R$ {sal_2:.2f}')
else:
    print(f'Seu salário de R$ {sal:.2f}, com o aumento de 10% passa a ser R$ {sal_1:.2f}')
