"""lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
print(len(lanche))"""


"""lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim'
for comida in lanche:  # para cada "comida" em "lanche":
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')"""


"""lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
for cont in range(0, len(lanche)):
    print(cont)"""


"""lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
for cont in range(0, len(lanche)):
    print(lanche[cont])"""


"""lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('')
for comida in lanche:  # A mesma coisa do for de cima
    print(f'Eu vou comer {comida}')"""


lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('')
for pos, comida in enumerate(lanche):  # A mesma coisa do for de cima
    print(f'Eu vou comer {comida} na posição {pos}')

