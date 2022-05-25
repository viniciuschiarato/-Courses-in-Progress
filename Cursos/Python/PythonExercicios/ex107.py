from package_mod import moeda_ex107

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda_ex107.metade(p)}')
print(f'O dobro de {p} é {moeda_ex107.dobro(p)}')
print(f'Aumentando 10%, temos {moeda_ex107.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda_ex107.diminuir(p, 13)}')
