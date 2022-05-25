from package_mod import moeda_ex109

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda_ex109.moeda(p)} é {moeda_ex109.metade(p, True)}')
print(f'O dobro de {moeda_ex109.moeda(p)} é {moeda_ex109.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda_ex109.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda_ex109.diminuir(p, 13, True)}')
