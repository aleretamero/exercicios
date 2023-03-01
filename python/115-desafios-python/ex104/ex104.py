# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de
# forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas
# um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(msg):
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro.\033[m')
    return valor


num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}')
