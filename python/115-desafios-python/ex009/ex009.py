# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

from time import sleep
n = int(input('Digite um número para ver sua tabuada: '))
linha = (25*'=')

sleep(.2)
print(linha)
print('ANALISANDO...           ')
print(linha)
sleep(1)

print('TABUADA DO NÚMERO {}'.format(n))

print(linha)
print(' {} X {:2} = {:>3}'.format(n, 1, (n*1)))
print(' {} X {:2} = {:>3}'.format(n, 2, (n*2)))
print(' {} X {:2} = {:>3}'.format(n, 3, (n*3)))
print(' {} X {:2} = {:>3}'.format(n, 4, (n*4)))
print(' {} X {:2} = {:>3}'.format(n, 5, (n*5)))
print(' {} X {:2} = {:>3}'.format(n, 6, (n*6)))
print(' {} X {:2} = {:>3}'.format(n, 7, (n*7)))
print(' {} X {:2} = {:>3}'.format(n, 8, (n*8)))
print(' {} X {:2} = {:>3}'.format(n, 9, (n*9)))
print(' {} X {:2} = {:>3}'.format(n, 10, (n*10)))
print(linha)
