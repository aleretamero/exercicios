# Um professor quer escolher um dos seus quatro alunos para apagar o quadro,
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice

alun1 = str(input('Primeiro aluno: '))
alun2 = str(input('Segundo aluno:  '))
alun3 = str(input('Terceiro aluno: '))
alun4 = str(input('Quarto aluno:   '))
lista = [alun1, alun2, alun3, alun4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
