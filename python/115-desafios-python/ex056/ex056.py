#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

from time import sleep

np = 4         #>>> Número de pessoas
idadetotal = 0
homemvelho = ''
idadehomem = 0
mulhernova = 0

for cont in range(1, np + 1):
    print('-~-~- {}º PESSOA -~-~-'.format(cont))
    nome =  str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo =  str(input('SEXO [M/F]: ')).strip().upper()
    idadetotal = idadetotal + idade
    if sexo == 'M':
        if idade > idadehomem:
            homemvelho = nome
            idadehomem = idade
    elif sexo == 'F' and idade < 20:
        mulhernova += 1
    elif sexo != 'M' and sexo != 'F':
        print('ERRO NA ESCOLHA DO SEXO')
media = idadetotal / np
sleep(.5)
print('\nANALISANDO...')
sleep(1)
print('\nDe acordo com os dados análisados:'
      '\nA média de idade do grupo é de {:.1f} anos'
      '\nO homem mais velho é o {} com {} anos'
      '\nPossui {} mulher(es) com menos de 20 anos'.format(media, homemvelho, idadehomem, mulhernova))
