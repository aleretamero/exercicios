# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
# com a formatação correta.

# variavel
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# alimentação da matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input((f'Digite um valor para [{l}, {c}]: ')))
print('=-=' * 10)
# formatação da matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
