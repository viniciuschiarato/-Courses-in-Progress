# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que
# estão na tupla.
from random import randint
"""a = randint(1, 9)
b = randint(1, 9)
c = randint(1, 9)
d = randint(1, 9)
e = randint(1, 9)
t = (a, b, c, d, e)
contador = menor = maior = 0
print(f'Os valores soretados foram: ', end='')
for c in t:
    print(f'{c} ', end='')
    contador += 1
    if contador == 1:
        menor = c
        maior = c
    else:
        if c < menor:
            menor = c
        elif c > maior:
            maior = c
print(f'\nO maior valor soretado foi: {maior}')
print(f'O menor valor soretado foi: {menor}')"""

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores soretados foram: ', end='')
for elemento in numeros:
    print(f'{elemento} ', end='')
print(f'\nO maior valor soretado foi: {max(numeros)}')
print(f'O menor valor soretado foi: {min(numeros)}')