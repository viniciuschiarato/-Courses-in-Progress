# Exercício Python 102: Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional) indicando se
# será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n=1, show=False):
    """
    -> Calcule o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a memória de cálculo.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            if c == 1:
                print('=', end=' ')
        f *= c
    print(f)


num = int(input('Digite o número para saber seu fatorial: '))
fatorial(num)
help(fatorial)
