# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
# Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

from time import sleep

linha = '-=' * 25

print(linha)
print('\33[7;30m{:^50}\33[m'.format('CALCULADORA IMC'))
print(linha)
peso = float(input('Digite aqui seu PESO:   '))
altura = float(input('Digite aqui sua ALTURA: '))
if altura > 10:
    altura = altura / 100
imc = (peso / (altura ** 2))
print(linha)

sleep(.5)
print('\33[7;30m{:<50}\33[m'.format('ANALISANDO...'))
sleep(2)
print(linha)

if imc < 18.5:
    status = '\33[7;32m ABAIXO DO PESO \33[m'
elif imc >= 18.5 and imc < 25:
    status = '\33[7;32m PESO IDEAL \33[m'
elif imc >= 25 and imc < 30:
    status = '\33[7;33m SOBRE PESO \33[m'
elif imc >= 30 and imc < 40:
    status = '\33[7;31m OBESIDADE \33[m'
elif imc >= 40:
    status = '\33[7;31m OBESIDADE MÓRBIDA \33[m'

print('O seu IMC está em {:.2f}'.format(imc))
print('Você está na categoria {}.'.format(status))
print(linha)
