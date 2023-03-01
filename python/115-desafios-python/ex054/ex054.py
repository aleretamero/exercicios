# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

linha = '-~-' * 12

maior = 0
menor = 0
print(linha)
for cont in range(1, 8, 1):
    nasc = int(input('EM QUE ANO A {}º PESSOA NASCEU? '.format(cont)))
    if date.today().year - nasc >= 21:
        maior = maior + 1
    elif date.today().year - nasc < 21:
        menor = menor + 1
print(linha)
print('TIVEMOS {} MAIOR(ES) DE IDADE '
      '\nTIVEMOS {} MAIOR(ES) DE IDADE'.format(maior, menor))
print(linha)
