# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
linha = '=-=' * 10
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('OPÇÃO INVÁLIDA')
    if continuar in 'N':
        break
print(linha)
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números')
print(f'A ordem decrescente dos valores é {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
