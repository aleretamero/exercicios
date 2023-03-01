# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados
# pela função anterior.

from random import randint
from time import sleep


def sorteia():
    print('Sortenado 5 valores da lista:', end=' ')
    for c in range(0, 5):
        c = randint(0, 9)
        numeros.append(c)
        print(f'{c}', end=' ')
        sleep(.5)
    print('PRONTO!')


def somaPar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numeros}, temos {soma}')


numeros = []

sorteia()
somaPar()
