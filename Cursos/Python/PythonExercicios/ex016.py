# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo
# teclado e mostre na tela a sua porção Inteira.
"""import math
num = float(input('Digite um valor: '))
v = math.trunc(num)
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, v))"""

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
