# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for ímpar, desconsidere-o.

linha = '=~=' * 16
soma = 0

print(linha)
for cont in range(1, 7):
    num = int(input('Digite o {}º número >>> '.format(cont)))
    if num % 2 == 0:
        soma += num
print(linha)
print('A soma dos números pares digitados é >>> {}'.format(soma))
print(linha)
