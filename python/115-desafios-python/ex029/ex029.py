# Escreva um programa que leia a velocidade de um carro. -Se ele ultrapassar 80Km/,
# mostre uma mensagem dizendo que ele foi multado. -A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual a velocidade atual do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!')
