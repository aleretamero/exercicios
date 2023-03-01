# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento

sal = float(input('Qual é o salário do funcionário? R$'))
aum = (sal * 0.15)
saln = (sal + aum)
print('Um funcionário que ganhava R${:.2f}, com aumento de 15% passa a receber R${:.2f}'.format(
    sal, saln))
