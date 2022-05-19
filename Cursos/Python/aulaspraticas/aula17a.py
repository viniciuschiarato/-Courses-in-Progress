num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7 em python esse comando não adiciona valores a lista. Mas em PHP sim.
num.append(7)  # adiciona valores ao final da lista
num.sort()  # coloca em ordem
num.sort(reverse=True)  # coloca em ordem ao contrario
num.insert(2, 0)  # adiciona valores a lista conforme indicado no parenteses na posição 2 adicionar 0
num.pop()  # remove o último elemento da lista
num.pop(2)  # remove o elemento da lista indicado no parenteses
print(num)
print(f'Essa lista tem {len(num)} elementos.')
valores = list(range(4, 11))
print(valores)
