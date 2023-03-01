# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('Por favor digite 3 número')
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número:  '))
num3 = int(input('Terceiro número: '))

lista = [num1, num2, num3]
menor = min(lista)
maior = max(lista)

# if num1 >= num2 and num1 >= num3:
#    maior = num1
# if num1 <= num2 and num1 <= num3:
#    menor = num1
#
# if num2 >= num1 and num2 >= num3:
#    maior = num2
# if num2 <= num1 and num2 <= num3:
#    menor = num2
#
# if num3 >= num1 and num3 >= num2:
#    maior = num3
# if num3 <= num1 and num3 <= num2:
#    menor = num3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
