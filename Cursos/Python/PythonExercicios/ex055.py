#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 99999
for p in range(1, 6):
    peso = float(input('Informe o peso da {}° pessoa: (kg) '.format(p)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido foi {}kg'.format(maior))
print('O menor peso lido foi {}kg'.format(menor))
