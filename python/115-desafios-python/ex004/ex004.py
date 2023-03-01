# Código para digitar algo e obter informações sobre o que foi digitado.

from time import sleep

linha = '-=' * 25
print(linha)
t1 = input('Digite algo: ')
sleep(.2)
print(linha)
print('ANALISANDO DADOS...')
print(linha)
sleep(1)

print('O tipo primitivo desse valor é ', type(t1))
print('Só tem espaços?                ', t1.isspace())
print('É um número?                   ', t1.isnumeric())
print('É alfabético?                  ', t1.isalpha())
print('É alfanúmerico?                ', t1.isalnum())
print('Está em maiúsculas?            ', t1.isupper())
print('Está em minúsculas?            ', t1.islower())
print('Está capitalizada?             ', t1.istitle())
print(linha)
