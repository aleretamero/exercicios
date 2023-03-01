# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
linha = '=-=' * 15
tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG',
          'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
          'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avai', 'Juventude')

print(linha)
print('Lista de times do brasileirão', tabela)
print(linha)
print('Os cinco primeiros são:', tabela[:5])
print(linha)
print('Os quatro últimos são:', tabela[-4:])
print(linha)
print('Times em ordem alfabética:', sorted(tabela))
print(linha)
print('O Avai está na {}ª posição.'.format(tabela.index('Avai') + 1))
