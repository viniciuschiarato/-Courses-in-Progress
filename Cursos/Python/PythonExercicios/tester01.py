from random import choice
jogada = choice(range(1, 4))
lista = [[1, 'Pedra'], [2, 'Papel'], [3, 'tesoura']]

print('Vamos jogar pedra, papel e tesoura?')
print('Escolhasua opção:')
print('1 - Pedra \n2 - Papel \n3 - Tesoura')
while True:
    try:
        jogador = int(input('Informe sua jogada: '))
        if jogador > 3 or jogador < 0:
            jogador = ''
        int(jogador)
    except ValueError:
        print('\033[31mErro resposta inválida.\033[m')
    else:
        break
escolha_pc = escolha_player = 0
for poss in lista:
    if jogada == poss[0]:
        escolha_pc = poss[1]
    if jogador == poss[0]:
        escolha_player = poss[1]
print(f'Eu escolhi {escolha_pc} e você {escolha_player}')
