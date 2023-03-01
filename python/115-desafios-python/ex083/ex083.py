# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses
# abertos e fechados na ordem correta.

expr = str(input('Digite uma expressão: ')).strip()
quant = []

for valor in expr:
    if valor == '(':
        quant.append(valor)
    elif valor == ')':
        if len(quant) > 0:
            quant.pop()
        else:
            quant.append(valor)
            break
if len(quant) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')
