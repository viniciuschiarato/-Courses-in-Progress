valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:  # Para cada "v" (Valor) em "Valores"
    print(f'{v}...', end='')

# se eu quiser a chave (indice/posição dos valores)
for i, v in enumerate(valores):  # i de indice
    print(f'Na posição {i} encontrei o valor {v}!')
print('Cheguei ao final da lista')
