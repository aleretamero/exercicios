# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar.
# Considere US$1,00 = R$3,27.

linha = '-=' * 25
print(linha)
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = float(real/3.27)
print(linha)
print('Com R${:.2f} você pode comprar US${:.2f}'.format(
    real, dolar))
print(linha)
