from lib.interface import *
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do programa'])
    print(resposta)
    if resposta == 1:
        print(linha())
        print('OPÇÃO 1'.center(30))
        print(linha())
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
