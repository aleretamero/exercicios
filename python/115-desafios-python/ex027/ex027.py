# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = str(input('Digite seu nome completo: ')).strip().title()
indiv = nome.split()

print('Seu primeiro nome é: {} \nSeu último nome é: {}'.format(
    indiv[0], indiv[-1]))
