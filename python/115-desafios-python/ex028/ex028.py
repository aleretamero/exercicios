# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#  e peça para o usuário descobrir qual foi o número escolhido pelo computador.
# -O programa deverá escrever na tela se o usúario venceu ou perdeu.

from time import sleep
from random import randint
computador = randint(0, 5)  # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente advinhar...')
print('-=-' * 20)
sleep(0.2)
jogador = int(input('Em que número eu pensei? '))
sleep(0.2)
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print(f'PERDEU! Eu pensei no número {computador} e não no {jogador}!')
