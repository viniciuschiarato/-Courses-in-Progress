# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1>n2:
    l = n1
else:
    l = n2
if n1>n3:
    s = n1
else:
    s = n3
if l>s:
    r = l
else:
    r = s
print('O maior número {:.0f}'.format(r))
if n1<n2:
    l1 = n1
else:
    l1 = n2
if n1<n3:
    s1 = n1
else:
    s1 = n3
if l1<s1:
    r = l1
else:
    r = s1
print('O menor número {:.0f}'.format(r))'''

'''a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>b and c>a:
    maior = c
print('\nO menor número digitado é: {}\n\nE o maior número é: {}'.format(menor, maior))'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\nO maior valor é {} e o menor é {}.'.format(maior, menor), end=' ')
