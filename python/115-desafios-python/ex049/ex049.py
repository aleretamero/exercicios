# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

linha = '=' * 20

print('{:=^20}'.format(' TABUADA '))
num = int(input('Digite um número p/'
                '\nsaber sua tabuada:'
                '\n>>> '))

# int(input('Digite o valor do multiplo inicial'    >>>>>>para usuario escolher multiplo inicial
numinicio = 1
#        '\n>>> '))
# int(input('Digite o valor do multiplo final'      >>>>>>para usuario escolher multiplo final
numfinal = 10
#       '\n>>> '))

print(linha)
multiplo = 0
for cont in range(numinicio, numfinal + 1):
    multiplo += 1
    if cont % 2 == 0:
        print('\033[7;30m {:<3} X {:>3}  = {:>5} \033[m'.format(
            num, multiplo, num * multiplo))
    elif cont % 2 == 1:
        print('\033[47m {:<3} X {:>3}  = {:>5} \033[m'.format(
            num, multiplo, num * multiplo))
print(linha)
