# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

from time import sleep

linha = '-=' * 30

print(linha)
print('\33[7;30m{:^60}\33[m'.format('ANALISADOR DE TRIÂNGULOS'))
print(linha)

n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento:  '))
n3 = float(input('Terceiro segmento: '))
print(linha)
sleep(.4)
print('{:<30}'.format('ANALISANDO...'))
sleep(1.5)
print(linha)

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    if n1 == n2 == n3:
        print('Os segmentos acima podem formar um triângulo EQUILÁTERO.')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Os segmentos acima podem formar um triângulo ISÓSCELES.')
    else:
        print('Os segmentos acima podem formar um triângulo ESCALENO.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
print(linha)
