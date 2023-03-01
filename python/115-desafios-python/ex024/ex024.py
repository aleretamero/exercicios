# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com "SANTO".

cidade = str(input('Escreva o nome de uma cidade :')).strip()
cidade = cidade.upper()
print('O nome da cidade começa com SANTO?', "SANTO" in cidade[0:5])
# print(cidade)
