#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time
num = int(random.randint(0, 5))
print('\nNeste momento estou pensando em um número entre 0 e 5.')
print('\nQuer tentar adivinhar?')
resp = int(input('\nDigite seu palpite: '))
print('\nProcessando...')
time.sleep(3)
if resp == num:
    print('\nVocê acertou!')
else:
    print('\nkkkkk, não era esse número que eu estava pensando.\nEu pensei no {}'.format(num))
