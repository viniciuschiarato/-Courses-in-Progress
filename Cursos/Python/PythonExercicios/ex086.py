# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com
# valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""entrada = list()
listalinhas = list()
listamacro = list()
for contador in range(0, 3):
    for linha1 in range(0, 3):
        entrada.append(int(input(f'Digite um valor para [{contador}, {linha1}]: ')))
        listalinhas.append(entrada[:])
        entrada.clear()
    listamacro.append(listalinhas[:])
    listalinhas.clear()
for q in range(0, 3):
    for p in range(0, 3):
        print(f' {listamacro[q][p]} ', end=' ')
    print()"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('=-'*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
