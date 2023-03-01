# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre
# a lista ordenada na tela.
listnumeros = []
for count in range(0, 5):
    num = (int(input(f'\nDigite um valor: ')))
    if count == 0:
        listnumeros.append(num)
        print('Adicionado na lista...')
    elif num > listnumeros[-1]:
        listnumeros.append(num)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(listnumeros):
            if num <= listnumeros[pos]:
                listnumeros.insert(pos, num)
                print(f'Foi adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'\nOs valores digitados em ordem foram {listnumeros}')
