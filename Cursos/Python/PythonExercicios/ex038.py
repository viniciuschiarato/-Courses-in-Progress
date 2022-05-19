#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 < n2:
    primeironumero = 'menor'
    segundonumero = 'maior'
    print('O primeiro valor é {}'.format(primeironumero))
    print('O segundo valor é {}'.format(segundonumero))
elif n1 > n2:
    primeironumero = 'maior'
    segundonumero = 'menor'
    print('O primeiro valor é {}'.format(primeironumero))
    print('O segundo valor é {}'.format(segundonumero))
else:
    print('Não exite valor maior, os dois são iguais')


