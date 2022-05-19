# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
"""entrada = list()
listalinhas = list()
listamacro = list()
pares = list()
coluna3 = list()
somapares = somacoluna3 = 0
for contador in range(0, 3):
    for linha1 in range(0, 3):
        entrada = (int(input(f'Digite um valor para [{contador}, {linha1}]: ')))
        listalinhas.append(entrada)
    listamacro.append(listalinhas[:])
    listalinhas.clear()
for q in range(0, 3):
    for p in range(0, 3):
        print(f'[{listamacro[q][p]:^3}]', end=' ')
    print()
for q in range(0, 3):
    for v in listamacro[q]:
        if v % 2 == 0:
            pares.append(v)
for v in pares:
    somapares += v
print(f'A soma dos valores pares é: {somapares}')
for q in range(0, 3):
    coluna3.append(listamacro[q][2])
for v in coluna3:
    somacoluna3 += v
print(f'A soma do valores da coluna 3 é: {somacoluna3}')
print(f'O maior valor da segunda linha é: {max(listamacro[1])}')"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('=-'*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
