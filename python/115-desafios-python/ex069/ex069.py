# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
linha = '-' * 25
mais18 = homens = mulhermenos20 = 0

while True:
    print('{} \n {:^25} \n{}'.format(linha, 'CADASTRAR PESSOA', linha))
    idade = int(input('IDADE: '))
    while True:
        sexo = str(input('SEXO: [M/F] ')).strip().upper()[0]
        if sexo in 'MF':
            break
        else:
            print('OPÇÃO INVÁLIDA')
    if idade > 18:
        mais18 += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulhermenos20 += 1
    while True:
        print(linha)
        continuar = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('OPÇÃO INVÁLIDA')
    if continuar in 'N':
        break
print(f'{linha}'
      f'\nTotal de pessoas maior de 18 anos cadastradas: {mais18}'
      f'\nTotal de Homens cadastrados: {homens}'
      f'\nTotas de Mulheres menor que 20 anos cadastradas: {mulhermenos20}')
