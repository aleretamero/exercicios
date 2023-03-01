def moeda(preco=0, moed='R$'):
    r = str(f'{moed}{preco:>.2f}').replace('.', ',')
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


#num = int(input())
#por = int(input('%'))
#print(diminuir(num, por))

