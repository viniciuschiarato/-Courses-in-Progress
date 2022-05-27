def file_search(name):
    if file_exist(name):
        print(f'File found.')
    else:
        print(f'File not found.')
        new_file(name)


def file_exist(name):
    try:
        a = open(name, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def new_file(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('There was an error creating the file.')
    else:
        print(f"Created {name} file.")


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


def menu(lista):
    while True:
        cont = 0
        option = ''
        print('-'*30)
        print('MAIN MENU'.center(30))
        print('-'*30)
        for v in lista:
            cont += 1
            print(f'{lc(3)}{cont} - {lc(4)}{v}')
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


lista_menu_ex115 = ['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do programa']
file_search('test_search.txt')
menu(lista_menu_ex115)
