# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10
# primeiros termos da progressão usando a estrutura while.

linha = '=' * 40
print('{:=^40}'.format('PROGRESSÃO ARITIMÉTICA'))
termo = int(input('Digite o 1º termo: \n>>> '))
razao = int(input('Digite a razão: \n>>> '))
cont = 1

while cont <= 10:
    print(f'{termo}', end='')
    print('→ 'if cont < 10 else '...', end='')
    termo = termo + razao
    cont = cont + 1

# print('FIM')
print('\n', linha)
