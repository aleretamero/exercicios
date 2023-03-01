# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
linha = '-~' * 22

print(linha)
print('{:^44}'.format('JOKENPÔ'))
print(linha)
print('DIGITE 1 PARA PAPEL')
print('DIGITE 2 PARA PEDRA')
print('DIGITE 3 PARA TESOURA')
jogador = int(input('DIGITE AQUI: '))
cpu = randint(1, 3)
print(linha)

# escolha do Jogador
if jogador == 1:
    print('O jogador escolheu PAPEL')
elif jogador == 2:
    print('O jogador escolheu PEDRA')
elif jogador == 3:
    print('O jogador escolheu TESOURA')
else:
    print('Digito errado, por favor reinicie o jogo!')

# escolha da CPU
if jogador == 1 or jogador == 2 or jogador == 3:
    if cpu == 1:
        print('O Computador escolheu PAPEL')
    elif cpu == 2:
        print('O computador escolheu PEDRA')
    elif cpu == 3:
        print('O computador escolheu TESOURA')
    print(linha)

# resultado
if jogador == 1 and cpu == 2 or jogador == 2 and cpu == 3 or jogador == 3 and cpu == 1:
    print('A VITÓRIA FOI DO JOGADOR')
elif cpu == 1 and jogador == 2 or cpu == 2 and jogador == 3 or cpu == 3 and jogador == 1:
    print('A VITÓRIA FOI DO COMPUTADOR')
elif jogador == cpu:
    print('A PARTIDA TERMINOU EM EMPATE')
print(linha)
