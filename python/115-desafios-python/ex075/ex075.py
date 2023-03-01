# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
par = 0

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
num4 = int(input('Digite um número: '))
nums = (num1, num2, num3, num4)

print('Você digitou os números:', end=' ')
for count in nums:
    print(count, end=' ')
    if count % 2 == 0:
        par += 1
print('')
if nums.count(9) == 1:
    print(f'O número 9 apareceu {nums.count(9)} vez')
elif nums.count(9) > 1:
    print(f'O número 9 apareceu {nums.count(9)} vezes')
if 3 in nums:
    print(
        f'O número primeiro número 3 apareceu na {nums.index(3) + 1}ª posição')
if par > 0:
    print('Os números pares digitados foram:', end=' ')
    for count in nums:
        if count % 2 == 0:
            print(count, end=' ')
