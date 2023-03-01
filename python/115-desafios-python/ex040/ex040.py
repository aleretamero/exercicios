# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO


linha = ('-' * 40)

print(linha)
print('{:^40}'.format('SISTEMA DE MÉDIA DE NOTA'))
print(linha)
n1 = float(input('INFORME A NOTA DO PRIMEIRO SEMESTRE: '))
n2 = float(input('INFORME A NOTA DO SEGUNDO SEMESTRE:  '))
print(linha)

media = (n1 + n2) / 2
if media < 5:
    print('\33[7;31m REPROVADO! \33[m Sua nota média foi {:.1f}'.format(media))
elif media >= 7:
    print('\33[7;32m APROVADO! \33[m Sua nota média foi {:.1f}'.format(media))
else:
    print('\33[7;33m RECUPERAÇÃO! \33[m Sua média foi {:.1f}'.format(media))
print(linha)
