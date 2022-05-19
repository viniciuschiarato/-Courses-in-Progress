# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
"""geral = list()
pares = list()
impares = list()
entrada = 0
for contador in range(1, 8):
    entrada = int(input(f'Digite o {contador}° número: '))
    if entrada % 2 == 0:
        pares.append(entrada)
    else:
        impares.append(entrada)
geral.append(pares[:])
geral.append(impares[:])
geral[0].sort()
geral[1].sort()
print(geral)
print(f'Os valores pares digitados foram: {sorted(geral[0])}')
print(f'Os valores ímpares digitados foram: {sorted(geral[1])}')"""

num = [[], []]
valores = 0
for c in range(0, 8):
    valor = int(input(f'Digite o {c+1}° valor: '))
    if valor %2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print('=-'*30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
