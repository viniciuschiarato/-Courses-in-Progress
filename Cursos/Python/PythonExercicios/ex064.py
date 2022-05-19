# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

'''n = soma = contador = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    contador = contador + 1
    soma = soma + n
print('Você digitou {} números e a soma dentre eles foi {}.'.format(contador - 1, soma-999))'''

n = soma = contador = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    contador = contador + 1
    soma = soma + n
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma dentre eles foi {}.'.format(contador, soma))