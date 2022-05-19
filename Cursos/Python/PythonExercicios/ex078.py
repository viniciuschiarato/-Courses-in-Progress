# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
maior = menor = 0
lista = list()
for contador in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {contador}: ')))
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}... ', end='')
