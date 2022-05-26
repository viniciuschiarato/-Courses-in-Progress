def metade(n, f=False):
    n /= 2
    if f:
        return moeda(n)
    else:
        return n


def dobro(n, f=False):
    n *= 2
    if f:
        return moeda(n)
    else:
        return n


def aumentar(n, porcentagem, f=False):
    aumento = n
    porcentagem /= 100
    aumento *= porcentagem
    n += aumento
    if f:
        return moeda(n)
    else:
        return n


def diminuir(n, porcentagem, f=False):
    aumento = n
    porcentagem /= 100
    aumento *= porcentagem
    n -= aumento
    if f:
        return moeda(n)
    else:
        return n


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')
