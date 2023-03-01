# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


def contador(a, b, c):
    if c == 0:
        c = 1
    if a > b:
        b -= 1
    elif a < b:
        b += 1
    if a > b and c > 0 or a < b and c < 0:
        c *= -1
    for c in range(a, b, c):
        print(c, end=' ')
        sleep(.3)
    print('FIM!')


print('=-=' * 10)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print('=-=' * 10)
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)
print('=-=' * 10)
print('Agora é sua vez de personalizar a contagem!')
pa = int(input('Início: '))
pb = int(input('Fim:    '))
pc = int(input('Passo:  '))
if pc < 0:
    pc *= -1
elif pc == 0:
    pc = 1
print(f'Contagem de {pa} até {pb} de {pc} em {pc}')
contador(pa, pb, pc)
