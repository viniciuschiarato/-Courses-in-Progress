# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo em uma lista composta.
import random
import time
basededados = list(range(1, 61))
escolhas = numerodojogo = 0
palpites = list()
jogos = list()
numero = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, numero):
    while True:
        escolhas = (random.choice(basededados))
        if escolhas not in palpites:
            palpites.append(escolhas)
        if len(palpites) == 6:
            break
    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()
for v in jogos:
    numerodojogo += 1
    print(f'Jogo {numerodojogo}: {v}')
    time.sleep(1)
