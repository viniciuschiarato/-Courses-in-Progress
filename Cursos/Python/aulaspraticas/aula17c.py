# Posso começar uma lista das seguintes formas: list() ou variável = []
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
print(valores)
for chave, v in enumerate(valores):
    print(f'Na posição {chave} encontrei o valor: {v}')
print('fim')
