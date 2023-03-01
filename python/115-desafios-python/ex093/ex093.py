# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de
# futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
totgols = 0
linha = '=-=' * 20

jogador['nome'] = str(input('Nome do jogador? '))
partidas = int(input(f'Quanta partidas {jogador["nome"]} jogou? '))
for count in range(0, partidas):
    gol = (int(input(f'Quantos gols na {count + 1}º partida? ')))
    gols.append(gol)
    totgols += gol
jogador['gols'] = gols[:]
jogador['total'] = totgols

print(linha)
print(jogador)
print(linha)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(linha)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    => Na {c +1}º partida, fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {jogador["total"]} gols')
