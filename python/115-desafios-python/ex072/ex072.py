# Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número de zero a 20: '))
        if num < 0 or num > 20:
            print('Opção inválida')
        else:
            break
    print(f'Você digitou o número {extenso[num]}')
    while True:
        continuar = str(
            input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('Opção inválida')
    if continuar == 'N':
        break
print('PROGRAMA FINALIZADO')
