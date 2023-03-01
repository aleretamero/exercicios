# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual seu nome completo: ')).strip()
# nome = nome.upper()
# silva = nome[nome.find('SILVA') : nome.find('SILVA') + 5]
# print('Seu nome tem Silva?', silva == 'SILVA')
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))


# nome = nome.split()
# print(nome[nome.find('SILVA') : nome.find('SILVA') + 5 ])

# if (nome[nome.find('SILVA') : nome.find('SILVA') +5 ]) == 'SILVA':
#    print('Seu nome possui Silva')

# else:
#   print('Seu nome não possui Silva')
