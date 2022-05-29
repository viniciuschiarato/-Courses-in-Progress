from time import sleep


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
        file_open = open(name, 'rt')
    except:
        print('There was an error reading the file.')
    else:
        for line in file_open:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<23}{data[1]:>3} anos')
            sleep(1)


def include_text(file_id, name='Unknown', age=0):
    try:
        file = open(file_id, 'at+')
        name = str(input('Name: ')).title()
        age = read_int('Age: ')
    except:
        print('There error in opening file.')
    else:
        try:
            file.write(f'{name};{age}\n')
        except:
            print('TThere error in process of write files.')
        else:
            print(f'New register "{name}" added.')
            file.close()


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
            print(f'{content[0]}'.center(30))
            print('-' * 30)
            print_file_content('test_search.txt')
        if option == 2:
            print('-' * 30)
            print(f'{content[1]}'.center(30))
            print('-' * 30)
            include_text('test_search.txt')
        if option == 3:
            print('-' * 30)
            print('PROGRAM FINISH...'.center(30))
            print('THANK YOU!'.center(30))
            print('COME BACK SOON!'.center(30))
            print('-' * 30)
            break


file_name = 'test_search.txt'
file_search(file_name)
content = ['Check registered', 'New register', 'Exit program']
menu(content)
