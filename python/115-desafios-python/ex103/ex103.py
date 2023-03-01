# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba
# dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser
# capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome="<desconhecido>", gols=0):
    return f'O jogador {n} fez {g} gol(s) no campeonato.'


n = str(input('Nome do jogador: '))
g = int(input('número de gols:  '))
print(ficha(n, g))
