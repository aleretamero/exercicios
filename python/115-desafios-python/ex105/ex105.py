# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(*n, sit=False):
    """
    →→PROGRAMA PARA ANÁLISAR DADOS DE NOTAS←←
    :param n: Inserir uma ou mais notas
    :param sit : (opcional) Selecionar True para obter a situação
    :return: dicionário com os dados análisados das notas
    """
    r = dict()
    r['TOTAL'] = len(n)
    r['MAIOR'] = max(n)
    r['MENOR'] = min(n)
    r['MÉDIA'] = sum(n) / len(n)
    if sit:
        if r['MÉDIA'] < 5:
            r['SITUAÇÃO'] = 'RUIM'
        elif r['MÉDIA'] < 7:
            r['SITUAÇÃO'] = 'MÉDIA'
        else:
            r['SITUAÇÃO'] = 'BOA'
    return r


# Programa principal
resp = notas(4, 2, 4, 8, sit=True)
print(resp)
help(notas)
