def metade(n,):
    n /= 2
    return n


def dobro(n,):
    n *= 2
    return n


def aumentar(n, porcentagem,):
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


def moeda(n):
    return f'R${n:.2f}'
