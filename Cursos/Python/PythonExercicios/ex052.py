#Exercício Python 052: Faça um programa que leia um número
# inteiro e diga se ele é ou não um número primo.
'''numeroaleatorio = int(input('Digite um número inteiro para saber se ele é ou não um número primo: '))
contador = 0
for c in range(1, numeroaleatorio + 1):
    if numeroaleatorio % c == 0:
        print('\033[33m', end='')
        contador = contador + 1
        if contador >= 2:
            inf1 = 'vezes'
        else:
            inf1 = 'vez'
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')
print('\033[m\nO número {} foi dividido {} {}'.format(numeroaleatorio, contador, inf1))
if contador == 2:
    inf2 = 'é um número primo'.upper()
else:
    inf2 = 'não é um número primo'.upper()
print('O {} {}'.format(numeroaleatorio, inf2))'''

núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[34m', end=' ')
        tot += 1
        if tot > 1:
            inf1 = 'vezes'
        if tot > 2:
            inf2 = 'não é um número primo'
        else:
            inf2 = 'é um número primo'
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m\nO número {} foi divido {} {}'.format(núm, tot, inf1))
print('O {} {}'.format(núm, inf2))