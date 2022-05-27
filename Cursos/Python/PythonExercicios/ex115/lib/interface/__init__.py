def read_int(txt):
    while True:
        try:
            input_ = int(input(txt))
        except (ValueError, TypeError):
            print(f'\033[31mErro. O valor digitado não é um número inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mErro. Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return input_


def lc(color=0):
    if color != 0:
        return f'\033[3{color}m'
    else:
        return f'\033[m'
    # branco = 0
    # red = 1
    # green = 2
    # yellow = 3
    # blue = 4
    # magenta = 5
    # cian = 6
    # gray = 7


def linha(tam=30):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 0
    for v in lista:
        cont += 1
        print(f'{lc(3)}{cont} - {lc(4)}{v}')
    print(f'{lc(0)}{linha()}')
    opc = read_int('Sua opção: ')
    return opc
