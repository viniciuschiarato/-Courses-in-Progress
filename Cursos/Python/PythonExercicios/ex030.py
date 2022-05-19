#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
número = int(input('Digite um número inteiro e veja se ele é par ou impar: '))
if número % 2 == 0:
    print('O número {} é par'.format(número))
else:
    print('O número {} é impar'.format(número))



