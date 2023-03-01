# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois
# parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor
# lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(a=1, show=False):
    """
    -→ Calcula o Fatorial de um número
    :param a: O número a ser calculado
    :param show (opcional): Mostra ou não a conta
    :return: O valor fatorial de a
    """

    f = 1
    for c in range(a, 0, -1):
        if show:
            print(f'{c}', 'X' if c > 1 else '=', end=' ')
        f *= c
    return f


print(fatorial(5, True))
help(fatorial)
