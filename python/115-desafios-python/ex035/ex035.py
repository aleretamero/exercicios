# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
# um triângulo.
from time import sleep
print('-=' * 25)
print('Analisador de Triângulos')
print('-=' * 25)
num1 = float(input('Primeiro segmento: '))
num2 = float(input('Segundo segmento:  '))
num3 = float(input('Terceiro segmento: '))
print('-=' * 25)
sleep(0.2)
print('ANALISANDO...')
sleep(0.8)
if (num1 + num2) > num3 and (num1 + num3) > num2 and (num2 + num3) > num1:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
print('-=' * 25)
