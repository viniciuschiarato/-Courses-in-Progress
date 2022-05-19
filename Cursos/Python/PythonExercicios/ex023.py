#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""import random
n = random.randint(0, 9999)
s = str(n)
print(s)
#print('Milhar: '+(s[0]))
#print('Centena: '+(s[1]))
#print('Dezena: '+(s[2]))
#print('Unidade: '+(s[3]))
m = ('Milhar: ')
c = ('Centena: ')
d = ('Dezena: ')
u = ('Unidade: ')
print(('{:9}'.format(m)) + (s[0]))
print(('{:9}'.format(c)) + (s[1]))
print(('{:9}'.format(d)) + (s[2]))
print(('{:9}'.format(u)) + (s[3]))"""

num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
m1 = ('Milhar: ')
c2 = ('Centena: ')
d3 = ('Dezena: ')
u4 = ('Unidade: ')
print(('{:9}'.format(u4))+('{}'.format(u)))
print(('{:9}'.format(d3))+('{}'.format(d)))
print(('{:9}'.format(c2))+('{}'.format(c)))
print(('{:9}'.format(m1))+('{}'.format(m)))
'''print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))'''

