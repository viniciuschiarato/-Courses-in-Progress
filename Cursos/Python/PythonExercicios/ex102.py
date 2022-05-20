def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    if show:
num = int(input('Calculo de fatorial\n\nDigite o número para saber seu fatorial: '))
fatorial(num, show=False)
