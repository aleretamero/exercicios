# Exercício Python 095: aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()
jogador = dict()
gols = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().upper()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    jogador.clear()
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continuar in 'SN':
            break
        print('Seleciona S ou N')
    if continuar in 'N':
        break
print('><' * 20)
print(f'{"cod":<5}{"nome":<15}{"gols":<15}{"total":<5}')
print('-' * 40)

for k, v in enumerate(time):
    print(f'{k:^5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        break
    if dados >= len(time):
        print(f'Não existe dados para o jogador {dados}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[dados]["nome"]}')
        for k, v in enumerate(time[dados]["gols"]):
            print(f'   No {k + 1}ª jogo fez {v} gols')
print('  >>FIM<<  ')
