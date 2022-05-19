# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def area(l, c):
    r = larg * comp
    print(f'A área do terreno {comp:.1f} x {larg:.1f} é de {r:.1f}')


print()
print(f'{"Controle de terrenos":^30}')
print(f'-' * 30)
comp = float(input('Comprimento (m): '))
larg = float(input('Largura (m): '))
area(comp, larg)
