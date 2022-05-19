# Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens
# através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(a, b, c):
    print('=-'*30)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if b > a:
        b += 1
    if c < 0:
        c *= -1
    if b < a:
        b -= 1
        c *= -1
    if b == 0:
        b = -1
    if c == 0:
        c = 1
    for v in range(a, b, c):
        print(f'{v}', end=' ')
        sleep(0.5)
    print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem! ')
d = int(input('Início: '))
e = int(input('Fim: '))
f = int(input('Passo: '))
contador(d, e, f)
