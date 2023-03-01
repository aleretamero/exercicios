# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
# N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

linha = '-' * 40
print(linha)
print('{:^40}'.format('SEQUÊNCIA DE FIBONACCI'))
termo = int(input('Quantos termos você quer? '))
f1 = 0
f2 = 1
cont = 0
while cont != termo:
    if cont == 0:
        print(0, end=' → ')
    elif cont == 1:
        print(1, end=' → ')
    else:
        f = f1 + f2
        print(f, end=' → ')
        f1 = f2
        f2 = f
    cont += 1
print('FIM')
print(linha)
