# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

linha = ('-=' * 43)

print(linha)
print('\33[7;30m    POR FAVOR PREENCHA OS DADOS ABAIXO PARA ANALISAR SE O EMPRÉSTIMO SERA APROVADO    \33[m')
print(linha)
vcasa = (float(input('Qual o valor da casa que deseja compra? R$')))
salario = (float(input('Qual o seu salário? R$')))
tempoemp = (int(input('Quantos anos de emprestimos gostaria de fazer? ')))
print(linha)

parcela = vcasa / (tempoemp * 12)

if salario * 0.3 <= parcela:
    print('\33[7;31m  NEGADO! Nessas condiçoes sua parcela ficaria R${:.2f} excedendo 30% do seu salário  \33[m'.format(
        parcela))
else:
    print('\33[7;32m  PARABÉNS! Seu emprestimo foi APROVADO em {} parcelas de R${:.2f}  \33[m'.format(
        (tempoemp * 12), parcela))

print(linha)
