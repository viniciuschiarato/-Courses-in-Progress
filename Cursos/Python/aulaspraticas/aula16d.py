a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # Tupla "a" junto com a "b"
d = b + a  # Tupla "b" junto com a "a"
print(a)
print(b)
print(c)
print(d)
print(len(c))
print(c.count(5))
print(d)
print(d.index(8))  # Em que posição esta o "8"
print(d.index(2))  # O "2" esta na posição 3 e também na 4, o programa só reporta a 1° ocorrencia
print(d)
print(d.index(5))
print(d.index(5, 1))  # index "5" a partir da pocição 1 (Deslocamento)
