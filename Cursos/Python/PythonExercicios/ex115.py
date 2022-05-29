from time import sleep:


def file_search(name):
    try:
        file = open(name, "rt")
        file.close()
    except FileNotFoundError:
        file = False
    else:
        file = True
    if file:
        print(f'File found.')
    else:
        print(f'File not found.')
        new_file(name)


def new_file(name):
    try:
        file = open(name, 'wt+')
        file.close()
    except:
        print('There was an error creating the file.')
    else:
        print(f"Created {name} file.")


def print_file_content(name):
    try:
        file = open(name, 'rt')
    except:
        print('There was an error reading the file.')
    else:
        for linha in file:
            dados = linha.split(';')
            print(f'{dados[0]:<22}{dados[1]:>3} anos')
            sleep(1)


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
            print_file_content('test_search.txt')
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


content = ['check registered', 'New register', 'exit program']
menu(content)
file_name = 'test_search.txt'
file_search(file_name)
