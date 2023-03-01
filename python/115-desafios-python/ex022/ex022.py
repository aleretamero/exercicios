# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -O nome com todas as letras maiúsculas.
# -O nome com todas as letras minúsculas.
# -Quantas letras aparecem sem considerar  espaços.
# -Quantas letras tem o primeiro nome.

from time import sleep

nome = str(input('Digite seu nome completo: ')).strip()

sleep(0.5)
print('Analisando seu nome...')
sleep(1.5)
nomelista = nome.split()

print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome em minúsculas é', nome.lower())
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
print(
    f'Seu primeiro nome é {nomelista[0]} e ele tem {len(nomelista[0])} letras')
