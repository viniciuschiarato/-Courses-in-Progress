# TUPLAS (são variáveis imutáveis)
# É possivel começar uma variável comporsta de três maneiras
# EXPL: lanche = com (tupla), com [lista] e com {dicionário}.
"""lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')  # tupla in pytho2"""
lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim'  # tupla in python3
print(lanche)
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2])
print(lanche[-2:])
'''lanche[1] = 'Refrigerante'  # ERRO: Objetos do tipo 'Tupla' não podem ter itens assimilados(Tuplas são imutáveis)
print(lanche[1])'''
