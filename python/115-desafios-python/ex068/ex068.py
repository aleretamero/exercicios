# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

from random import randint

linha = '→←' * 30
linha2 = '-' * 60

print(linha)
print('{:^60}'.format('PAR OU IMPAR'))
print(linha)

resultado = ''
cont = 0

while True:
    jog = int(input('Digite um valor: '))
    cpu = randint(1, 10)
    while True:
        escolha = str(input('Par ou Ímpar ? [P/I] ')).strip().upper()[0]
        if escolha in 'PI':
            break
        else:
            print('OPÇÃO INVÁLIDA')
    if (jog + cpu) % 2 == 0:
        resultado = 'PAR'
    elif (jog + cpu) % 2 == 1:
        resultado = 'IMPAR'
    print(linha2)
    print(
        f'Você jogou {jog} e o computador jogou {cpu}. total de {jog + cpu} deu {resultado}')
    print(linha2)
    if escolha == resultado[0]:
        print('Você VENCEU')
        print('')
        cont += 1
    elif escolha != resultado[0]:
        print('Você PERDEU')
        break
if cont == 1:
    print(f'GAME OVER! Você venceu {cont} vez.')
else:
    print(f'GAME OVER! Você venceu {cont} vezes')
print(linha)
