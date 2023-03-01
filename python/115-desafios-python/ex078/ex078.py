# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros = []
maior = menor = 0
for n in range(0, 5):
    numeros.append(int(input(f'Digite um valor para posição {n}: ')))
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        elif numeros[n] < menor:
            menor = numeros[n]
print('=-=' * 15)
print(f'Você digitou os valores {numeros}')
print(f'O maior número foi {maior} nas posições', end=' ')
for contador, valor in enumerate(numeros):
    if valor == maior:
        print(f'{contador}...', end=' ')
print()
print(f'O menor número foi {menor} nas posições', end=' ')
for contador, valor in enumerate(numeros):
    if valor == menor:
        print(f'{contador}...', end=' ')
print()
