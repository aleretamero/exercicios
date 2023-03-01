# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
# pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade <= 15:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 15 < idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('=-=' * 10)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
