# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

# variaveis
listnumeros = [[], []]

for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        listnumeros[0].append(num)
    elif num % 2 == 1:
        listnumeros[1].append(num)

# Organizar ordem crescente
listnumeros[0].sort()
listnumeros[1].sort()
print('=-=' * 15)
print(f'Os valores pares digitados foram: {listnumeros[0]}')
print(f'Os valores ímpares digitados foram: {listnumeros[1]}')
