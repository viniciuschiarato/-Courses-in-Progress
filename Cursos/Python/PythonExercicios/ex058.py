#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''import random
import time
continuar = 0
contador = 1
num = int(random.randint(0, 5))
print('\nNeste momento estou pensando em um número entre 0 e 5.')
print('\nQuer tentar adivinhar?')
resp = int(input('\nDigite seu palpite: '))
print('\nProcessando...')
time.sleep(3)
if resp == num:
    print('\nVocê acertou!')
elif resp != num:
    while resp != num:
        print('\nNão era este número que eu estava pensando.')
        continuar = str(input('\nQuer continuar tando? [S/N]: ')).strip().upper()[0]
        contador += 1
        if continuar == 'N':
            resp = num
            print('\nOk, obrigado por jogar!')
        elif continuar == 'S':
            resp = int(input('\nTente outra vez: '))
            if resp == num:
                print('\nAgora você acertou!')
                print('Após {} tentativas.'.format(contador))
        else:
            print('Resposta invalida.')'''

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Um pouco menos... Tente mais uma vez.')
        elif jogador < computador:
            print('Um pouco mais... Tente mais uma vez.')
print('Acertou com {} tentativas, PARABÉNS!'.format(palpites))

