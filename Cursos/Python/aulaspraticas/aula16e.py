"""a = ('Esse', 'é')
pessoa = ('Gustavo', 39, 'M', 99.88)  # As tuplas em python não precisam ter dados de um mesmo tipo
print(a + pessoa)
del(pessoa)  # Apaga a tupla
print(a + pessoa)"""


a = ('Esse', 'é')
pessoa = ('Gustavo', 39, 'M', 99.88)  # As tuplas em python não precisam ter dados de um mesmo tipo
print(a + pessoa)
del(pessoa[0])  # NÃO vai apagar o elemento da posição 0 dentro da tupla
print(a + pessoa)
