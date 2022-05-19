# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma sequência de Fibonacci.
sequência = int(input('Informe quantos números da sequência de Fibonenacci você quer ver: '))
contador = 2
t1 = 0
t2 = 1
print('{} - {} '.format(t1 , t2), end='')
while contador != sequência:
    t3 = t1 + t2
    print('- {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    contador = contador + 1
print(' Fim')
