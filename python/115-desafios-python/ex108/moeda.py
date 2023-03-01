def moeda(preco=0, moeda='R$'):
    r = str(f'{moeda}{preco:>.2f}').replace('.', ',')
    return r


def aumentar(n=0, p=0):
    r = n + (p * n / 100)
    return r


def diminuir(n=0, p=0):
    r = n - (p * n / 100)
    return r


def dobro(n=0):
    r = n * 2
    return r


def metade(n=0):
    r = n / 2
    return r
