# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
linha = '=-=' * 10

cont = mais1000 = totcompra = menorpreco = 0
maisbarato = ''
while True:
    print(linha)
    print('{:^30}'.format('CADASTRAR PRODUTO?'))
    while True:
        cadastrar = int(input('[ 1 ] SIM'
                              '\n[ 2 ] NÃO'
                              '\n >>> '))
        if cadastrar == 1 or cadastrar == 2:
            break
        else:
            print('(OPÇÃO INVÁLIDA)')
    if cadastrar == 1:
        print('-' * 30)
        nome = str(input('NOME: ')).strip().upper()
        preco = float(input('PREÇO: R$'))
        if preco > 1000:
            mais1000 += 1
        totcompra += preco
        if cont == 0 or preco < menorpreco:
            maisbarato = nome
            menorpreco = preco
        cont += 1
    else:
        break
if cont > 0:
    print(f'Total gasto nas compras → R${totcompra:.2f}')
    print(f'Quantidade de produtos acima de R$1000.00 → {mais1000}')
    print(f'Produto mais barato → {maisbarato} no valor de R${menorpreco:.2f}')
print(linha)
