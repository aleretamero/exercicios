# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
cont = maior = menor = soma = 0
parar = False
while not parar:
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = num
        soma = num
        cont += 1
    elif cont > 0:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        soma += num
        cont += 1
    continuar = 0
    while continuar != 1:
        continuar = int(input('Inserir mais valores?'
                              '\n[ 1 ] SIM'
                              '\n[ 2 ] NÃO'
                              '\n>>>'))
        if continuar == 1:
            parar = False
        elif continuar == 2:
            parar = True
            continuar = 1
        else:
            print('OPÇÃO INVALIDA')
if cont == 1:
    print(f'A média do número digitado é {soma}')
else:
    print(f'A média entre os números digitados é {soma / cont}')
print(f'O maior valor digitado é {maior}')
print(f'O menor valor digitado é {menor}')
