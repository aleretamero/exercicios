# O mesmo professor do desafio anterior quer sotear a ordem de apresentação.
# De trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos.
# E mostre a ordem sorteada.

from random import shuffle

alun1 = str(input('Primeiro aluno: '))
alun2 = str(input('Segundo aluno:  '))
alun3 = str(input('Terceiro aluno: '))
alun4 = str(input('Quarto aluno:   '))
lista = [alun1, alun2, alun3, alun4]
shuffle(lista)
print('A ordem apresentada será \n{}'.format(lista))
