# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10
# primeiros termos da progressão usando a estrutura while.

linha = '=-=' * 15
print('{:=^45}'.format('PROGRESSÃO ARITIMÉTICA'))
termo = int(input('Digite o 1º termo: \n>>> '))
razao = int(input('Digite a razão: \n>>> '))
cont = 1
while cont < 11:
    print(f'{termo}', end='')
    print('→ 'if cont < 10 else '→ PAUSA', end='')
    termo = termo + razao
    cont = cont + 1
laco = False
while not laco:
    novotermo = int(input('\nQuantos termos você quer mostrar a mais? '))
    novocont = novotermo + cont
    if novotermo != 0:
        while novocont != cont:
            print(f'{termo}', end='')
            print('→ 'if cont + 1 < novocont else '→ PAUSA', end='')
            termo += razao
            cont += 1
    elif laco == 0:
        laco = True
print(f'Progressão finalizada com {cont - 1} termos')
print(linha)
