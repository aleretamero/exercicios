# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
# em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
c = 1
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}

print('Dados jogados')
sleep(1)
for k, v in jogadores.items():
    print(f'O jogador {k} tirou {v}')
    sleep(.5)
sleep(.5)

ranking = dict(
    sorted(jogadores.items(), key=lambda item: item[1], reverse=True))

print('Ranking dos jogadores:')
sleep(1)
for k, v in ranking.items():
    print(f'{c}ª lugar foi do {k} que tirou >>> {v} no dado')
    c += 1
    sleep(.5)
