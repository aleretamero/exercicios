# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)
cont = soma = 0
while True:
    num = int(input(f'Digite um número: [999 PARA PARAR] '))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print(f'Foram digitados {cont} e a soma deles é {soma}')
