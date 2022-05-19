# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.
"""dados = dict()
listagols = list()
dados['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, partidas):
    quantgol = int(input(f'Quantos gols na partida {c}? '))
    listagols.append(quantgol)
dados['gols'] = listagols
totgols = 0
for v in listagols:
    totgols += v
dados['total'] = totgols
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'  => Na partida {c}, fez {listagols[c]} gols.')
print(f'Foi um total de {totgols} gols.')"""

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'  Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
