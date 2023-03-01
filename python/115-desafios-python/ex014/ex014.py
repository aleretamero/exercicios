# Escreva um programa que converta uma temperatura digitada em °C para °F.

c = float(input('Informe a temperatura em °C: '))
f = float(c * (9 / 5) + 32)

print('A temperatura em {:.1f}°C corresponde a {:.1f}°F!'.format(c, f))
