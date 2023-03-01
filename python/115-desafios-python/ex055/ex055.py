# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

menor = 0
maior = 0
for cont in range(1, 6):
    peso = float(input('DIGITE AQUI O SEU PESO: '))
    if menor == 0 and maior == 0:
        menor = peso
        maior = peso
    elif peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso
print('O maior peso registrado é de {:.1f}kg '
      '\nO menor peso registrado é de {:.1f}Kg '.format(maior, menor))
