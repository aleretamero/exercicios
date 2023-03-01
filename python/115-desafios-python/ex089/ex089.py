# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada
# um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

listalunos = []
alunos = []
notas = []
medias = []
notasindiv = []
contador = procurar = 0
linha = '-' * 50

while True:
    alunos.append(str(input('Nome:')))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    notasindiv.append(n1)
    notasindiv.append(n2)
    medias.append((n1 + n2)/2)
    notas.append(notasindiv[:])
    notasindiv.clear()
    contador += 1
    while True:
        continuar = str(input('Quer continuar? ')).strip().upper()
        if continuar in 'SN':
            break
        else:
            print('OPÇÃO INVÁLIDA')
    if continuar in 'N':
        break

listalunos.append(alunos[:])
listalunos.append(notas[:])
listalunos.append(medias[:])
print('=-=' * 8)

print(f"{'Nº':<4}{'NOME':<15}{'MÉDIA':<5}")
print('-' * 24)
for c in range(0, contador):
    print(f'{c:<4}{listalunos[0][c]:<15}{listalunos[2][c]:>5.1f}')

while procurar != 999:
    print(linha)
    procurar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if procurar < contador:
        print(
            f"Notas de {listalunos[0][procurar]} são {listalunos[1][procurar]}")
    else:
        print()
print('FINALIZANDO...')
