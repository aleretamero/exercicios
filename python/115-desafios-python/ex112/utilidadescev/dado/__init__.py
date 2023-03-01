def leiaDinheiro(msg):
    valid = False
    while not valid:
        entrada = str(input(msg)).replace(',', '.').strip()
        validmsg = entrada.replace('.', '').isnumeric()
        if validmsg:
            valor = float(entrada)
            valid = True
            return valor
        else:
            print(f'\033[0;31mERRO! \"{entrada}\" é um preço inválido!\033[m')


def leiaInt(msg):
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro.\033[m')
    return valor


#n = leiaDinheiro('?')
#print(n)
