# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

# variaveis
listpessoas = []
listmulheres = []
listmaiorqmedia = []
pessoas = {}
media = somaidade = 0

# buscando dados
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    while True:
        if sexo in 'MF':
            break
        else:
            sexo = str(
                input('ERRO! Por favor, digite apenas M ou F. ')).strip().upper()
    idade = int(input('Idade: '))
    # alimentando dicionário
    pessoas['nome'] = nome
    pessoas['sexo'] = sexo
    pessoas['idade'] = idade
    # lista pessoas
    listpessoas.append(pessoas.copy())
    # lista mulheres
    if sexo in 'F':
        listmulheres.append(pessoas.copy())
    # média
    somaidade += idade
    media = somaidade / len(listpessoas)
    # maior que a média
    if idade > media:
        listmaiorqmedia.append(pessoas.copy())
    # limpando dicionário
    pessoas.clear()
    # continuar?
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while True:
        if continuar in 'SN':
            break
        else:
            continuar = str(
                input('ERRO! Responda apenas S ou N. ')).strip().upper()
    if continuar == 'N':
        break
# Respostas
print('=-=' * 15)
print(f'A) Ao todo temos {len(listpessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
if len(listmulheres) > 0:
    for c in listmulheres:
        print(f'[{c["nome"]}]', end=' ')
    print()
else:
    print('nenhuma')

print(f'D) Lista de pessoas que estão acima da média:')
for p in listpessoas:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
