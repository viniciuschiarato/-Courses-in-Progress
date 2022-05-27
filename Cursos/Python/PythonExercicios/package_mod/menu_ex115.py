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


def menu():
    print('-'*30)
    print('MENU PRINCIPAL'.center(30))
    print('-'*30)
    print(f'{lc(3)}1 - {lc(4)}Ver pessoas cadastradas')
    print(f'{lc(3)}2 - {lc(4)}Cadastrar novas pessoas')
    print(f'{lc(3)}3 - {lc(4)}Sair do sistema        ')
    print(f'{lc(0)}-' * 30)
    while True:
        try:

            option = int(input('Sua opção: '))
            if option not in range(1, 3):
                option = 'erro'
            int(option)
        except(ValueError, TypeError):
            print(f'{lc(1)}Erro! A opção informada é invalida.{lc()}')
            continue
        except KeyboardInterrupt:
            print(f'{lc(1)}Erro! Nenhuma opção informada.{lc()}')
            option = 3
            return option
        else:
            return option


print(menu())
