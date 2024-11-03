# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere o dólar a $ 5.87

n = float(input('Digite um valor para converter em dólar: R$ '))
dol = n / 5.87
print('Com R${:.2f}, você pode comprar ${:.2f} dólares. '.format(n, dol))
