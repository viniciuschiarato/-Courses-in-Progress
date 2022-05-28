from ex115.lib.interface import *
from time import sleep


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
        # print(a.read())  # .readlines (le e coloca toda a informação em uma linha)
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<22}{dados[1]:>3} anos')
            sleep(1)
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at+')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro durante o processo de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
