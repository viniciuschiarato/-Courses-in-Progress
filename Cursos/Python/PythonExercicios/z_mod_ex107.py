def metade(n):
    return n / 2


def dobro(n):
    return n * 2


def aumentar(n, porcentagem):
    aumento = n
    porcentagem /= 100
    aumento *= porcentagem
    n += aumento
    return n


def diminuir(n, porcentagem):
    aumento = n
    porcentagem /= 100
    aumento *= porcentagem
    n -= aumento
    return n
