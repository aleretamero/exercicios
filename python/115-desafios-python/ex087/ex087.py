# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3c = maior2l = 0

for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l][c] = num
        # soma pares
        if num % 2 == 0:
            somapar += num
        # soma coluna 3
        if c == 2:
            soma3c += num
        # maior linha 2
        if c == 0 and l == 1:
            maior2l = num
        else:
            if l == 1 and num > maior2l:
                maior2l = num
print('=-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-=' * 15)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {soma3c}')
print(f'O maior valor da segunda linha é {maior2l}')
