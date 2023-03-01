# Faça um programa que leia uma frase pelo teclado e mostre:
# -Quantas vezes aparece a letra "A".
# -Em que posição ela aparece a primeira vez.
# -Em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase aqui --> ')).upper().strip()

qt = frase.count('A')
prim = int(frase.find('A') + 1)
ult = int(frase.rfind('A') + 1)

print("""A letra 'A' aparece {} vezes.
A primeira letra 'A' apareceu na posição {}.
A última letra 'A' apareceu na posição {}.""".format(qt, prim, ult))
