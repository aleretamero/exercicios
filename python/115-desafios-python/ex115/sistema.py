from time import sleep
from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas',
                    'Cadastrar nova pessoa', 'Sair do sistema'], opcao=True)
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:  '))
        idade = str(leiaInt('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[0;31mERRO! Opção inválida.\033[m')
        sleep(1)
