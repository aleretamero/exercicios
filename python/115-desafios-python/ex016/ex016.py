# Crie um programa que leia um número real qualquer pelo teclado.
# E mostre na tela a sua porçao inteira.
# Ex: Digite um numero: 6.127.
# O numero 6.127 tem a parte inteira 6.

# Da para fazer com as funções math.trunc ou int também.

from math import floor
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, floor(num)))
