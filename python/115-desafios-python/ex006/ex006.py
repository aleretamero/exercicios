# Código para descobrir o dobro, triplo, e a raiz de um número.

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)

print('O dobro de {} vale {} \n O triplo de {} vale {} \n A raiz de {} é igual a {:.2f}'.format(
    n, d, n, t, n, r))
