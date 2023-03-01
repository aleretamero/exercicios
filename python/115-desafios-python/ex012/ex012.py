# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

valor = float(input('Qual é o preço do produto? R$'))
desc = float(valor-(valor * 0.05))

print('O produto que custava {:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(
    valor, desc))
