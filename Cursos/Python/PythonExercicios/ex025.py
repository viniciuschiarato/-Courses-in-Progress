#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
n = str(input('Digite seu nome: ')).strip()
u = (n.upper()) + " "
v = ('SILVA ' in u)
print('O nome digitado tem "Silva"?\nR: {}'.format(v))
