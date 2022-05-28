from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if arquivoexiste(arq):
    print(f'Arquivo encontrado.')
else:
    print(f'Arquivo não encontrado.')
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do programa'])
    print(resposta)
    if resposta == 1:
        leiaarquivo(arq)
    elif resposta == 2:
        print(linha())
        print('OPÇÃO 2'.center(30))
        print(linha())
    elif resposta == 3:
        print(linha())
        print('Saindo do sistema... Até logo!'.center(30))
        print(linha())
        break
    else:
        print(f'{lc(1)}Erro! A opção informada é invalida.{lc()}')
    sleep(2)
