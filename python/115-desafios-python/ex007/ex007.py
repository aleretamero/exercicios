# Código para calcular média.

from time import sleep

linha = '-=' * 25
print(linha)
print(' Digite as notas para obter a média               ')
n1 = float(input(' Primeira nota: '))
n2 = float(input(' Segunda nota:  '))
n3 = float(input(' Terceira nota: '))
n4 = float(input(' Quarta nota:   '))
sm = ((n1+n2+n3+n4)/4)
sleep(.2)

print(linha)
print(' ANALISANDO...                                    ')
print(linha)
sleep(1)

print(' A média de {:.1f}, {:.1f}, {:.1f} e {:.1f} é igual a {:.1f}'.format(
    n1, n2, n3, n4, sm))
print(linha)
