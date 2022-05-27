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
    while True:
        option = ''
        print('-'*30)
        print('MAIN MENU'.center(30))
        print('-'*30)
        print(f'{lc(3)}1 - {lc(4)}Ver pessoas cadastradas')
        print(f'{lc(3)}2 - {lc(4)}Cadastrar novas pessoas')
        print(f'{lc(3)}3 - {lc(4)}Sair do sistema        ')
        print(f'{lc(0)}-' * 30)
        while True:
            try:
                option = int(input('Sua opção: '))
                if option not in range(1, 4):
                    option = 'erro'
                int(option)
                break
            except(ValueError, TypeError):
                print(f'{lc(1)}Erro! A opção informada é invalida.{lc()}')
                continue
            except KeyboardInterrupt:
                print(f'{lc(1)}Nenhuma opção informada.{lc()}')
                option = 3
                break
        if option == 1:
            print('-' * 30)
            print('OPÇÃO 1'.center(30))
            print('-' * 30)
        if option == 2:
            print('-' * 30)
            print('OPÇÃO 2'.center(30))
            print('-' * 30)
        else:
            print('-' * 30)
            print('THANK YOU!'.center(30))
            print('COME BACK SOON!'.center(30))
            print('-' * 30)
            break


menu()

