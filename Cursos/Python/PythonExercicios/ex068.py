# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
"""from random import randint
from time import sleep
enunciado = 'VAMOS JOGAR PAR OU IMPAR???'
print('=-' * 30, f'\n{enunciado:^60}\n', '=-' * 30, )
numeroaleatorio = numerojogador = opcaojogador = soma = resultado = final = contador = 0
while True:
    numeroaleatorio = randint(1, 10)
    numerojogador = int(input('Digite um valor entre 1 e 10: '))
    if numerojogador > 10:
        numerojogador = int(input('Por favor escolha um número entre 1 e 10:'))
    elif numerojogador < 1:
        numerojogador = int(input('Por favor escolha um número entre 1 e 10:'))
    opcaojogador = str(input('Par ou Ìmpar? [P/I] ')).strip().upper()[0]
    if opcaojogador not in 'PI':
        opcaojogador = str(input('Opção inválida. Tente novamente.\nPar ou Ìmpar? [P/I]')).strip().upper()[0]
    contador += 1
    if opcaojogador == 'P':
        opcaojogador = 'PAR'
    if opcaojogador == 'I':
        opcaojogador = 'ÍMPAR'
    soma = numerojogador + numeroaleatorio
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print('Processando...')
    sleep(2)
    print(f'Você jogou {numerojogador} e eu joguei {numeroaleatorio}. O total da {soma} deu {resultado}')
    if resultado == opcaojogador:
        final = 'VOCÊ GANHOU!'
    else:
        final = 'Você perdeu!'
    print(final)
    if final == 'Você perdeu!':
        print(f'GAME OVER. Você venceu {contador - 1} vezes.')
    else:
        print('Vamos jogar novamente...')
        sleep(4)
    if final == 'Você perdeu!':
        break"""

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
    print('deu par.' if total % 2 == 0 else 'deu ímpar.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu.')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu.')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
