# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(a, b):
    print(f'A área de um terreno {a}x{b} é de {a * b}m²')


print('CONTROLE DE TERRENOS')
print('-' * 20)
l = float(input('LARGURA (m): '))
h = float(input('ALTURA (m): '))
área(l, h)
