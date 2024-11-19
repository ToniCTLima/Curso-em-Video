# Exercício 001 - Crie um programa que escreva 'Olá Mundo' na tela.

# Padrão ANSI para colocar cor no terminal \033[0;31;40m
# Códigos para estilo (style): 0, 1, 4, 7 - 0 sem estilo, 1 negrito, 4 sublinado, 7 inverte as configurações
# Códigos para cor no texto: 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 ciano, 37 cinza.
# Códigos para cor de background: 40 até 47 com a mesma sequência de cores do texto.

print('\033[1;35mOlá \033[m\033[34mMundo\033[m') 
