# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem
# por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostrá-lo por extenso.

"""numeros1 = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
numeros2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
entrada = int(input('Digite um número entre 0 e 20: '))
while entrada not in numeros2:
    entrada = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros1[entrada]}')"""

numeros1 = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
while True:
    entrada = int(input('Digite um número entre 0 e 20: '))
    if 0<= entrada <= 20:
        break
    print('Tente novamente.',end='')
print(f'Você digitou o número {numeros1[entrada]}')