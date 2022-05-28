from ex115.lib.interface import *
def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f"arquivo {nome} criado")


def leiaarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Error ao ler arquivo!')
    else:
        cabecalho('Pessoas Cadastradas')
        print(a.read())  # .readlines (le e coloca toda a informação em uma linha)
