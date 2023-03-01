# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta 2m².

linha = '-=' * 35

print(linha)
lar = float(input(' Largura da parede: '))
alt = float(input(' Altura da parede:  '))
print(linha)
area = float(lar * alt)
rend = 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(lar, alt, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(area / rend))
print(linha)
