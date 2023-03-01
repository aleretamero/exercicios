# Faça um programa que leia o comprimentro do cateto oposto e do cateto adjacente.
# De um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt, hypot

co = float(input('comprimento do cateto oposto:   '))
ca = float(input('comprimento do cateto adjacente '))
# hi = sqrt(co**2 + ca**2)
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))
