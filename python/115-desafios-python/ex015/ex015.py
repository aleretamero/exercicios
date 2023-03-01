# Escreva um programa que pergunte a quantidade de km percorridos por um carro
# alugado e a quantidade de dias pelo qual ele foi alufado. calcule o preço a
# pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km(s) rodados? '))

vkm = float(km * 0.15)
vdia = float(dia * 60)
total = (vdia + vkm)

print('O total a pagar é de R${:.2f}'.format(total))
