def resumo(preco=0, taxaa=0, taxad=0):
    linha = '-' * 30
    print(linha)
    print(f'{"RESUMO":^30}')
    print(linha)
    print(f'{"Preço analisado:":<20}{moeda(preco)}')
    print(f'{"Dobro do preço:":<20}{dobro(preco, f=True)}')
    print(f'{"Metade do preço:":<20}{metade(preco, f=True)}')
    print(f'{taxaa:<3}{"% de aumento:":<17}{aumentar(preco, taxaa, f=True)}')
    print(f'{taxad:<3}{"% de redução:":<17}{diminuir(preco, taxad, f=True)}')
    print(linha)


def moeda(preco=0, moed='R$'):
    r = str(f'{moed}{preco:>8.2f}').replace('.', ',')
    return r


def aumentar(n=0, p=0, f=False):
    r = n + (p * n / 100)
    return r if f is False else moeda(r)


def diminuir(n=0, p=0, f=False):
    r = n - (p * n / 100)
    return r if f is False else moeda(r)


def dobro(n=0, f=False):
    r = n * 2
    return r if f is False else moeda(r)


def metade(n=0, f=False):
    r = n / 2
    return r if f is False else moeda(r)
