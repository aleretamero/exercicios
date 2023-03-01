# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER


linha = ('-' * 40)

print(linha)
print('\33[7;30m{:^40}\33[m'.format('IDENTIFICADOR DE CATEGORIA'))
print(linha)
idade = int(input('INFORME A IDADE: '))
print(linha)

if idade <= 9:
    categoria = 'MIRIM'
elif idade > 9 and idade <= 14:
    categoria = 'INFANTIL'
elif idade > 14 and idade <= 19:
    categoria = 'JUNIOR'
elif idade == 20:
    categoria = 'SÊNIOR'
elif idade > 20:
    categoria = 'MASTER'

print('Você pertence a categoria \33[4m{}\33[m'.format(categoria))
print(linha)
