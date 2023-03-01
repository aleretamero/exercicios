# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e
# dizer qual deles é o maior.
from time import sleep


def maior(*num):
    if num == '':
        num = 0
    print('=-=' * 20)
    print('Analisando os valores passados...')
    cont = 0
    while cont < len(num):
        print(num[cont], end=' ')
        sleep(.4)
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {max(num)}')


maior(2, 9, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
