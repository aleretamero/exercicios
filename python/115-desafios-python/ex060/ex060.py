# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from time import sleep

# num = int(input('Digite um número para saber seu fatorial: '))
# cont = num
# resultado = 1
# print(f'Calculando {num}! = ', end='')
# while cont > 0:
#    print(f'{cont} ', end='')
#    print('X' if cont > 1 else '=', end=' ')
#    resultado *= cont
#    cont -= 1
# print(f'{resultado}')

num = int(input('Digite um número para saber seu fatorial: '))
multiplo = 1
print(f'Calculando {num}! =', end='')
sleep(.5)
for cont in range(num, 0, -1):
    multiplo = multiplo * cont
    print(' {} '.format(cont), end='')
    print('X' if cont > 1 else '= ', end='')
print(multiplo)
