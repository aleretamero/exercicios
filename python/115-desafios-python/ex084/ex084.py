# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando
# tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# Variaveis
contador = maiorp = menorp = 0
pessoas = []
dados = []

while True:
    dados.append(str(input('Nome: ')))
    peso = float(input('Peso: '))
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    if contador == 0:
        maiorp = menorp = peso
    elif contador > 0:
        if peso > maiorp:
            maiorp = peso
        elif peso < menorp:
            menorp = peso
    contador += 1
# Continuar loop
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continuar in 'SN':
            break
        else:
            print('Opção Inválida')
    if continuar in 'N':
        break
print('=-=' * 10)
# A)
if contador == 1:
    print(f'Ao todo, você cadastrou {contador} pessoa.')
elif contador > 1:
    print(f'Ao todo, você cadastrou {contador} pessoas.')
# B)
print(f"O maior peso foi de {maiorp:.1f}Kg. Peso de", end=' ')
for p in pessoas:
    if maiorp == p[1]:
        print(f'[{p[0]}] ', end=' ')
print()
# C)
print(f"O menor peso foi de {menorp:.1f}Kg. Peso de", end=' ')
for p in pessoas:
    if menorp == p[1]:
        print(f'[{p[0]}]', end=' ')
print()
