import z_mod_ex107

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {z_mod_ex107.metade(p):.2f}')
print(f'O dobro de {p} é {z_mod_ex107.dobro(p):.2f}')
print(f'Aumentando 10%, temos {z_mod_ex107.aumentar(p, 10):.2f}')
print(f'Reduzindo 13%, temos {z_mod_ex107.diminuir(p, 13):.2f}')
