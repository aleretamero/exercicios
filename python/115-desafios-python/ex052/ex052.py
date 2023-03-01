# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número para saber se ele é primo'
                '\n>>> '))
divid = 0
for cont in range(1, num + 1):
    if num % cont == 0:
        print('\033[32m', end='')
        divid = divid + 1
    else:
        print('\033[m', end='')
    print(cont, end=' ')
print('\033[m')
print('O número {} foi dividido {} vezes'.format(num, divid))
if divid == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')
