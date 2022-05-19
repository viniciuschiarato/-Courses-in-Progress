"""a = [2, 3, 4, 7]
b = a
b[2] = 8  # Peculiaridade do Python: As duas lista são auteras em simultaneo
# devido a ligação feita pelo sinal de igual na linha de cima
print(f'Lista A: {a}')
print(f'Lista A: {b}')"""

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8  # agora não exite mais a ligação de igualdade entre a e b
print(f'Lista A: {a}')
print(f'Lista A: {b}')
