# Exercício Python 48: Faça um programa que calcule a soma entre todos os números impares que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.

quant = 0
soma = 0
for count in range(1, 501, 2):
    if count % 3 == 0:
        soma += count
        quant += 1
print('A soma de todos os {} valores solicitados é {}'.format(quant, soma))
