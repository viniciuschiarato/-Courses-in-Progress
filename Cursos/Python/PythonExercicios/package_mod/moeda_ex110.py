def metade(n, f=False):
    n /= 2
    if f:
        return f'R${n:.2f}'
    else:
        return n


def dobro(n, f=False):
    n *= 2
    if f:
        return f'R${n:.2f}'
    else:
        return n


def aumentar(n, porcentagem, f=False):
    aumento = n
    porcentagem /= 100
    aumento *= porcentagem
    n += aumento
    if f:
        return f'R${n:.2f}'
    else:
        return n


def diminuir(n, porcentagem, f=False):
    aumento = n
    porcentagem /= 100
    aumento *= porcentagem
    n -= aumento
    if f:
        return f'R${n:.2f}'
    else:
        return n


def moeda(n):
    return f'R${n:.2f}'


def linha():
    print('-'*30)


def desc_lista(msg):
    return f'{msg:20}'


def printvalor(valor):
    return f'{valor:10}'


def resumo(n1, porc_aum='', porc_dim=''):
    linha()
    print(f'{"RESUMO DO VALOR":^30}')
    linha()
    print(f'{desc_lista("Preço analizado:")}', end='')
    print(printvalor(moeda(n1)))
    print(f'{desc_lista("Metade do preço:")}', end='')
    print(printvalor(metade(n1, f=True)))
    print(f'{desc_lista("Dobro do preço:")}', end='')
    print(printvalor(dobro(n1, f=True)))
    if porc_aum != '':
        print(f'{desc_lista(f"{porc_aum}% de aumento:")}', end='')
        print(printvalor(aumentar(n1, porc_aum, f=True)))
    if porc_dim != '':
        print(f'{desc_lista(f"{porc_dim}% de redução:")}', end='')
        print(printvalor(diminuir(n1, porc_dim, f=True)))
    linha()
