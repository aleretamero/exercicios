# Faça um programa que leia um ângulo qualquer e mostre na tela.
# O valor de seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo que você deseja: '))

rad = radians(ang)
se = sin(rad)
co = cos(rad)
tg = tan(rad)

print('O ângulo de {} tem o SENO     de {:.2f}'.format(ang, se))
print('O ângulo de {} tem o COSSENO  de {:.2f}'.format(ang, co))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tg))
