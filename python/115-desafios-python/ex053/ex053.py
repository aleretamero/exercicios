# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:


linha = '=~=' * 20
print(linha)
print('{:=^60}'.format('Análisador de palíndromo'))
texto = str(input('Digite uma frase:')).strip().upper()
quebra = texto.split()
junto = ''.join(quebra)
inverso = ''

for cont in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[cont]

print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um PALÍNDROMO')
else:
    print('Não temos um palíndromo')
