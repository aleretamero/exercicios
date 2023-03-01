# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = 0
soma = 0
parar = False
while not parar:
    num = int(input('Digite um número [999 PARA PARAR]: '))
    if num == 999:
        parar = True
    else:
        cont += 1
        soma += num
print(f'Você digitou {cont} números e a soma entre eles é {soma}')
