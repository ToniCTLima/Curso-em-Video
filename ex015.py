# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelo quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

km = float(input('Digite a a quilometragem rodada: '))
dias = int(input('Digite por quantos dias o carro esteve alugado: '))
a_pagar = km * 0.15 + 60 * dias
print(f'O carro andou por {km:.2f}km e esteve alugado por {dias} dias, o valor total a ser pago é R$ {a_pagar:.2f}.')
