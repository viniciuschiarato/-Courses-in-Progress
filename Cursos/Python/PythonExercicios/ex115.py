def file_exist(name):
    try:
        file_ = open(name, "rt")
        file_.close()
    except FileNotFoundError:
        return False
    else:
        return True


def file_search(name):
    if file_exist(name):
        print(f'File found.')
    else:
        print(f'File not found.')
        new_file(name)


def new_file(name):
    try:
        file_ = open(name, 'wt+')
        file_.close()
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
        option = ''
        print('-' * 30)
        print('MAIN MENU'.center(30))
        print('-' * 30)
        count = 0
        for v in lista:
            count += 1
            print(f'{lc(3)}{count} - {lc(4)}{v}')
        print(f'{lc(0)}-' * 30)
        while True:
            try:
                option = int(input('Select option: '))
                if option not in range(1, 4):
                    option = 'erro'
                int(option)
                break
            except(ValueError, TypeError):
                print(f'{lc(1)}Error! Invalid option.{lc()}')
                continue
            except KeyboardInterrupt:
                print(f'{lc(1)}no option selected.{lc()}')
                option = 3
                break
        if option == 1:
            print('-' * 30)
            print(f'{lista[0]}'.center(30))
            print('-' * 30)
        if option == 2:
            print('-' * 30)
            print(f'{lista[0]}'.center(30))
            print('-' * 30)
        if option == 3:
            print('-' * 30)
            print('PROGRAM FINISH...'.center(30))
            print('THANK YOU!'.center(30))
            print('COME BACK SOON!'.center(30))
            print('-' * 30)
            break


lista_menu_ex115 = ['check registered', 'New register', 'exit program']
file_exist('test_search.txt')
menu(lista_menu_ex115)
