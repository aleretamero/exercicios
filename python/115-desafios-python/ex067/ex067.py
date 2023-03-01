# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

cont = 1
while True:
    num = int(input('Quer ver a tabuada de qual valor: '))
    if num < 0:
        break
    print('-' * 20)
    while cont <= 10:
        print(f'{num} X {cont} = {num * cont}')
        cont += 1
    print('-' * 20)
    cont = 1
