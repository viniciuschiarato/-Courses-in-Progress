def input_pers():
    lista = list()
    v = str(input('Digite um preço: R$')).strip()  # .replace(' ', '')
    while v.isalpha() or v == '' or v.isspace():
        print(f'\033[31mErro, "{v}" não é um preço válido.\033[m')
        v = str(input('Digite um preço: R$')).strip()
    if ',' or '.' in v:
        lista.append(float(v.replace(',', '.')))
    return lista[0]


