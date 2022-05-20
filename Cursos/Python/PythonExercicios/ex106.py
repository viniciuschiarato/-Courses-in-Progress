def printpers(inp):
    lent = len(inp)
    # print('\033[7m', end='')
    print('-' * lent)
    print(f'{inp}')
    print('-' * lent)


def pyhelp():
    while True:
        printpers(f'{"PYHELP":^90}')
        input_ = str(input('Pesquise pela pelo nome dafunção ou biblioteca: ')).strip().lower()
        if input_ == 'fim':
            break
        help(input_)


pyhelp()
