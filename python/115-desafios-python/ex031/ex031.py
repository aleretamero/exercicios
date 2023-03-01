# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule e peça o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R#0,45 para viagens mais longas.

viagem = float(input('Qual a distância da viagem em Km? '))
print('Você está prestes a começar uma viagem de {:.2f}km'.format(viagem))
preco = (viagem * 0.50) if viagem <= 200 else (viagem * 0.45)
print('O valor da viagem será R${:.2f}'.format(preco))
