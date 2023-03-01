# Faça um programa que leia um número de 0 a 9999 e mostre
# na tela cada um dos digitos separados.
# Ex: Digite um número: 1834
# unidade:4
# dezena:3
# centena:8
# milhar:1

from time import sleep

num = str(input('Informe um número: ')).strip()
num = '0000' + num
sleep(0.2)
print('Analisando o número {} ...'.format(num[-4:]))
sleep(1.5)
print(
    f'Unidade: {num[-1]} \nDezena:  {num[-2]} \nCentena: {num[-3]} \nMilhar:  {num[-4]}')
