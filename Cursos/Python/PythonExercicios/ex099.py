# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

listavalores = list()


def maior(* valores):
    listavalores.clear()
    for c in valores:
        listavalores.append(c)
    print('=-' * 60)
    print('Analisando valores passados...')
    sleep(1)
    for c in listavalores:
        print(f'{c}', end=' ')
        sleep(0.5)
    sleep(0.5)
    print(f'Foram informados {len(listavalores)} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {max(listavalores)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
