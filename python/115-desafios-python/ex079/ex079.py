# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
listnumeros = []
while True:
    num = (int(input('Digite um valor: ')))
    if num in listnumeros:
        print('Valor duplicado! Não adicionado...')
    else:
        listnumeros.append(num)
        print('Valor adicionado com sucesso...')
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('OPÇÃO INVÁLIDA')
    if continuar in 'N':
        break
listnumeros.sort()
print(f'Você digitou os valores {listnumeros}')
