# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""database = list()
jogador = dict()
listagols = list()
partidas = soma = cont = 0
while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
    for p in range(0, partidas):
        gols = (int(input(f'Quantos gols na partida {p}? ')))
        listagols.append(gols)
        soma += gols
    jogador['Gols'] = listagols[:]
    jogador['Total'] = soma
    database.append(jogador.copy())
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('\033[31mInválido.\033[m Quer inserir ouro aluno? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('-' * 26)
        break
    else:
        listagols.clear()
        print('-' * 26)
print('-='*30)
print(f'{"Cod":<4}{"NOME":<15}{"GOLS":<15}{"TOTAL":<6}')
for i, j in enumerate(database):
    print(f'{i:<4}', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print(database)
while True:
    while True:
        visualizacao = int(input('Quer ver detalhes de algum jogador? Digite o código dele(999 para encerrar): '))
        if visualizacao in range(0, len(database)):
            break
        print('\033[31mCód inválido.\033[m')
    if visualizacao == 999:
        break
    print(database[visualizacao])"""

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERROR! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
