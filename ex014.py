# Escreva um programa que converta uma temperatura digitada em C° e converta para F°.

cel = float(input('Digite a tempertura em graus C° para converter em F°: '))
c_f = ((9 * cel) / 5) + 32
print('A temperatura de {}c°, corresponde a {}f°'.format(cel, c_f))