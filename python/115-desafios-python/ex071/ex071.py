# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
not50 = not20 = not10 = not1 = 0
linha = '=' * 40

print(linha)
print('{:^40}'.format('BANCO PYTHON'))
print(linha)
valor = float(input('Qual valor deseja sacar? R$'))
while True:
    while valor > 0:
        if valor % 50 == 0:
            valor -= 50
            not50 += 1
            break
        elif valor % 20 == 0:
            valor -= 20
            not20 += 1
            break
        elif valor % 10 == 0:
            valor -= 10
            not10 += 1
            break
        elif valor > 0:
            valor -= 1
            not1 += 1
            break
    if valor == 0:
        break
if not50 > 0:
    print(f'Total de {not50} cédulas de R$50')
if not20 > 0:
    print(f'Total de {not20} cédulas de R$20')
if not10 > 0:
    print(f'Total de {not10} cédulas de R$10')
if not1 > 0:
    print(f'Total de {not1} cédulas de R$1')
print(linha)
