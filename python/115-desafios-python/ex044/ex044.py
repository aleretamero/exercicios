# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

linha1 = '-=' * 35
linha2 = '_' * 70
linha3 = '=' * 70
cor = {'limpa': '\033[m',
       'pb': '\033[7;30m'}

print(linha1)
print('{}{:^70}{}'.format(cor['pb'], 'TITULO', cor['limpa']))
print(linha1)

valor = float(input('INFORME O VALOR DO PRODUTO: R$'))
print('DIGITE 1 PARA PAGAMENTO COM DINHEIRO')
print('DIGITE 2 PARA PAGAMENTO COM CARTÂO')
pag = int(input())
print(linha3)

if pag == 1:
    print('O valor do produto ficou R${:.2f} você ganhou 10% de desconto.'.format(
        valor - (valor * 0.1)))
elif pag == 2:
    print('DIGITE 1 PARA PAGAMENTO A VISTÁ')
    print('DIGITE 2 PARA PAGAMENTO EM 2X')
    print('DIGITE 3 PARA PAGAMENTO EM 3X')
    vezes = int(input())
    print(linha3)
    if vezes == 1:
        print('O valor do produto ficou R${:.2f} você ganhou 5% de desconto.'.format(
            valor - (valor * 0.05)))
    elif vezes == 2:
        print('O valor do produto ficou 2X de R${:.2f}'.format(valor / 2))
    elif vezes == 3:
        print('O valor do produto ficou 3X de R${:.2f} teve um aumento de 20%'.format(
            (valor + (valor * 0.2)) / 3))
    else:
        print('ERRO no digito, por favor reinicie o cálculo.')
else:
    print('ERRO no digito, por favor reinicie o cálculo.')
print(linha3)
