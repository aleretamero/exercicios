from ex115.lib.valid_dados import *


def linha(tam=45):
    return '-' * tam


def cabeçalho(msg='TITULO'):
    print(linha())
    print(msg.center(45))
    print(linha())


def menu(lista, opcao=False):
    cabeçalho('SISTEMA ARQUIVO 1.0')
    cont = 1
    for valor in lista:
        print(f'{cont} → {valor}')
        cont += 1
    print(linha())
    if opcao:
        opc = leiaInt('Defina opção: ')
        return opc

