# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo em uma lista composta.

# Modulos
from random import randint
from time import sleep

# Variaveis
linha = '-' * 40
listajogos = []
nums = []
contador = 0

# Titulo
print(linha)
print(f"{'MEGA SENA':^40}")
print(linha)
# Perguntando a quantidade de jogos
qjogo = int(input('Quantos jogo você  quer que sorteie? '))

# Mensagem de quantos jogos
if qjogo == 1:
    print(f"{'SORTEANDO 1 JOGO':=^40}")
    sleep(1.5)
elif qjogo > 1:
    text = f'SORTEANDO {qjogo} JOGOS'
    print(f"{text:=^40}")
    sleep(1.5)
else:
    print('NENHUM JOGO SORTEADO')

# Quantidade de listas/jogos
for jogo in range(0, qjogo):
    listajogos.append(list())

# Definindo cada jogo
while True:
    if contador == qjogo:
        break
    nsorte = randint(1, 60)
    if nsorte not in nums and len(nums) < 6:
        nums.append(nsorte)
        nums.sort()
    elif nums not in listajogos and len(nums) == 6:
        listajogos[contador] = nums[:]
        nums.clear()
        contador += 1

# Mostrando a Mensagem
if qjogo > 0:
    for c, v in enumerate(listajogos):
        print(f'Jogo {c + 1}: {v}')
        sleep(.5)
    print(f"{' < BOA SORTE! > ':=^40}")
