# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date
linha = ('-=' * 25)
print(linha)
print('\033[7;30m          PROGRAMA DE ALISTAMENTO MILITAR         \33[m')
print(linha)
nasc = int(input('INFORME O ANO DE NASCIMENTO: '))
print(linha)
idade = (date.today().year - nasc)

if idade == 18:
    print('VOCÊ DEVE SE ALISTAR NESTE ANO!!!')
elif idade < 18:
    print('VOCÊ DEVERÁ SE ALISTAR DAQUI A {} ANO(S)!!!'.format(18 - idade))
else:
    print('SEU PRAZO DE ALISTAMENTO ESTÁ ATRASADO {} ANO(S)!!!'.format(idade - 18))

print(linha)
