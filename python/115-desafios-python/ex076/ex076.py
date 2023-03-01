# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
count = 1
linha = '-' * 40

print(linha)
print('{:^40}'.format('LISATAGEM DE PREÇOS'))
print(linha)

for c in produtos:
    if count % 2 == 1:
        print('{:.<30}'.format(c), end='')
        count += 1
    elif count % 2 == 0:
        print('R${:8.2f}'.format(c))
        count += 1
print(linha)
