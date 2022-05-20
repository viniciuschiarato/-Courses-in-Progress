def fatorial(n=1, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        print(f'{c}', end=' ')
        if c > 1:
            print('x', end=' ')
        if c == 1:
            print('=', end=' ')
    print(f)


num = int(input('Calculo de fatorial\n\nDigite o número para saber seu fatorial: '))
fatorial(num, show=False)
