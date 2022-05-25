from package_mod import moeda_ex108

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda_ex108.moeda(p)} é {moeda_ex108.moeda(moeda_ex108.metade(p))}')
print(f'O dobro de {moeda_ex108.moeda(p)} é {moeda_ex108.moeda(moeda_ex108.dobro(p))}')
print(f'Aumentando 10%, temos {moeda_ex108.moeda(moeda_ex108.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda_ex108.moeda(moeda_ex108.diminuir(p, 13))}')
