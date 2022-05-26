def input_pers():
    lista = list()
    v = str(input('Digite um preço: R$')).strip()
    while v.isalpha() or v == '':
        print(f'\033[31mErro, "{v}" não é um preço válido.\033[m')
        v = str(input('Digite um preço: R$'))
    if ',' or '.' in v:
        lista.append(float(v.replace(',', '.')))
    return lista[0]


