# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

linha = '=' * 40

print('{:=^40}'.format('PROGRESSÃO ARITIMÉTICA'))

primeirot = int(input('Digite o 1º termo:'
                      '\n>>> '))
razao = int(input('Digite a razão:'
                  '\n>>> '))

print(linha)
for count in range(primeirot, primeirot + razao * 10, razao):
    print(count, end=' ')
print('')
print(linha)
