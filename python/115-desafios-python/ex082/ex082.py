# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

listnumeros = []
pares = []
impares = []
linha = '=-=' * 10

print(linha)
while True:
    listnumeros.append(int(input('Digite um valor: ')))
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if continuar in 'SN':
            break
        else:
            print('OPÇÃO INVÁLIDA')
    if continuar in 'N':
        break
print(linha)

for valor in listnumeros:
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)

print(f'A lista completa é {listnumeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
