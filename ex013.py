# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

sa = float(input('Digite o seu salário R$ '))
au = sa * (1 + 0.15)
print('Seu salário de R$ {:.2f}, com o aumento de 15% passará a ser R$ {:.21150f}'.format(sa, au))
