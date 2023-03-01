# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

linha = '→←' * 30
print(linha)
print('{:^60}'.format('INSIRA DOIS VALORES'))
valor1 = int(input('1º VALOR >>> '))
valor2 = int(input('2º VALOR >>> '))
print('\n')
print('{:^60}'.format('SELECIONE UMA OPÇÃO'))
opcao = int(input('[ 1 ] SOMAR'
                  '\n[ 2 ] MULTIPLICAR'
                  '\n[ 3 ] MAIOR'
                  '\n[ 4 ] NOVOS NÚMEROS'
                  '\n[ 5 ] SAIR DO PROGRAMA'
                  '\n>>> '))

while opcao != 5:
    if opcao == 1:
        print(
            f'A soma do valor {valor1} com valor {valor2} é igual a {valor1 + valor2}')
        print('\nDESEJA CONTINUAR?')
        opcao2 = int(input('[ 1 ] SIM'
                           '\n[ 2 ] NÃO'
                           '\n>>> '))
        while not opcao2 in (1, 2):
            print('OPÇÃO INVÁLIDA')
            opcao2 = int(input('[ 1 ] SIM'
                               '\n[ 2 ] NÃO'
                               '\n>>> '))
        if opcao2 == 1:
            opcao = 4
        elif opcao2 == 2:
            opcao = 5

    elif opcao == 2:
        print(
            f'A multiplicação do valor {valor1} com valor {valor2} é igual a {valor1 * valor2}')
        print('\nDESEJA CONTINUAR?')
        opcao2 = int(input('[ 1 ] SIM'
                           '\n[ 2 ] NÃO'
                           '\n>>> '))
        while not opcao2 in (1, 2):
            print('OPÇÃO INVÁLIDA')
            opcao2 = int(input('[ 1 ] SIM'
                               '\n[ 2 ] NÃO'
                               '\n>>> '))
        if opcao2 == 1:
            opcao = 4
        elif opcao2 == 2:
            opcao = 5

    elif opcao == 3:
        if valor1 > valor2:
            print(f'O maior valor foi o 1º= {valor1}')
        elif valor1 < valor2:
            print(f'O maior valor foi o 2º= {valor2}')
        elif valor1 == valor2:
            print(f'Ambos valores são iguais a {valor1}')
        print('\nDESEJA CONTINUAR?')
        opcao2 = int(input('[ 1 ] SIM'
                           '\n[ 2 ] NÃO'
                           '\n>>> '))
        while not opcao2 in (1, 2):
            print('OPÇÃO INVÁLIDA')
            opcao2 = int(input('[ 1 ] SIM'
                               '\n[ 2 ] NÃO'
                               '\n>>> '))
        if opcao2 == 1:
            opcao = 4
        elif opcao2 == 2:
            opcao = 5

    elif opcao == 4:
        print(linha)
        print('{:^60}'.format('INSIRA DOIS VALORES'))
        valor1 = int(input('1º VALOR >>> '))
        valor2 = int(input('2º VALOR >>> '))
        print('\n', linha)
        print('{:^60}'.format('SELECIONE UMA OPÇÃO'))
        opcao = int(input('[ 1 ] SOMAR'
                          '\n[ 2 ] MULTIPLICAR'
                          '\n[ 3 ] MAIOR'
                          '\n[ 4 ] NOVOS NÚMEROS'
                          '\n[ 5 ] SAIR DO PROGRAMA'
                          '\n>>>'))
    else:
        print('OPÇÃO INVÁLIDA')
        print('')
        opcao = 4

print('\n{:^60}'.format('OBRIGADO POR UTILIZAR O PROGRAMA'))
print(linha)
