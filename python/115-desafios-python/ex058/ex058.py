# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer.
from random import randint
from time import sleep

tentativas = 1
linha = '-=-' * 20

print(linha)
print('{:^60}'.format('Vou pensar em um número de 0 a 5 tente adivinhar...'))
# print(linha)
sleep(.2)
jog = int(input('Em que número eu pensei? '))
cpu = randint(0, 5)
sleep(.2)
print('ANALISANDO...')
sleep(.5)
print(linha)
while not cpu == jog:
    if jog < 0 or jog > 5:
        jog = int(input('digito inválido, tente novamente: '))
        cpu = randint(0, 5)
        sleep(.5)
    else:
        jog = int(input(f'Eu pensei em {cpu}, você PERDEU, '
                        f'\nmas tente novamente: '))
        cpu = randint(0, 5)
        sleep(.5)
        tentativas += 1
print(linha)
if tentativas == 1:
    print(f'Você VENCEU e só precisou de 1 tentativa PARABÉNS')
elif tentativas > 1 and tentativas < 5:
    print(f'Você VENCEU e só precisou de {tentativas} tentativas')
else:
    print(f'Você VENCEU, mas também com {tentativas} tentativas até minha vó')
print(linha)
