# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


linha = ('-=' * 35)

print(linha)
print('\33[7;30m{:^70}\33[m'.format('CONVERSOR DE NÚMEROS'))
print(linha)
num1 = int(input('Digite um número inteiro: '))
num2 = int(
    input('Digite 1 para conversão BINÁRIO, 2 para OCTAL e 3 para HEXADECIMAL: '))
print(linha)

if num2 == 1:
    binario = bin(num1)[2:]
    print('A conversão do número inteiro {} para binário é {}'.format(num1, binario))
elif num2 == 2:
    octal = oct(num1)[2:]
    print('A conversão do número inteiro {} para octal é {}'.format(num1, octal))
elif num2 == 3:
    hexa = hex(num1)[2:]
    print('A conversão do número inteiro {} para hexadecimal é {}'.format(num1, hexa))

print(linha)
