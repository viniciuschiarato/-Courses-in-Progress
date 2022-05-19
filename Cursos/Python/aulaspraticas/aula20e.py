def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def soma(*valores):
    s = 0
    for n in valores:
        s += n
    print(f'Somando os valores {valores} temos {s}!')


soma(2, 1, 7)
soma(8, 0)
soma(4, 4, 7, 6, 2)
