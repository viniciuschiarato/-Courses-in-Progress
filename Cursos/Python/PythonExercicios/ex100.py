# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados
# pela função anterior.

from random import randint
from time import sleep
numeros = list()


def sorteio():
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print('Sorteando 5 valores da lista:', end=' ')
    for v in numeros:
        print(f'{v}', end=' ')
        sleep(0.5)
    print('Pronto!')


def somapares():
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {numeros} temos {soma}')


sorteio()
somapares()
