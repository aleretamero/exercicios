# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# 7 >= aprovado 7 < reprovado

dados = {}

dados['nome'] = str(input('Nome: '))
dados['media'] = float(input('Média: '))
if dados['media'] >= 7:
    dados['situacao'] = 'APROVADO'
elif 7 > dados['media'] >= 5:
    dados['situacao'] = 'RECUPERAÇÃO'
else:
    dados['situacao'] = 'REPROVADO'

for k, v in dados.items():
    print(f'{k} é igual a {v}')
