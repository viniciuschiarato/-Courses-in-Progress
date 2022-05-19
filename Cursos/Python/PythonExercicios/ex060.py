#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

#n = int(input('Digite um número para calcular seu fatorial: '))
#mult = n
#print('{} x '.format(n), end='')
#for c in range(n-1, 0, -1):
    #print('{}'.format(c), end='')
    #print(' x ' if c > 1 else ' = ',end='')
    #mult = mult * c
#print('O fatorial de {} é {}.'.format(n, mult))

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))