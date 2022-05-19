# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
listatimes = ('Santos', 'Atlético-MG', 'Corinthians', 'Cuiabá-MT', 'Internacional', 'Avaí',
              'Red Bull Bragantino', 'Palmeiras', 'Flamengo', 'Coritiba', 'São Paulo', 'Botafogo',
              'Fluminense', 'América-MG', 'Ceará', 'Athletico PR', 'Atlético-GO', 'Goiás', 'Juventude',
              'Fortaleza')
a = 'São Paulo'
print('-=' * 30)
print(f'Lista de times do brasileirão: {listatimes}')
print('-=' * 30)
print(f'Os 5 primeiros são: {listatimes[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são: {listatimes[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(listatimes)}')
print('-=' * 30)
print(f'O time {listatimes[10]} esta na {(listatimes.index(a)) + 1}° posição.')
print(f'O time {listatimes[10]} esta na {(listatimes.index("São Paulo")) + 1}° posição.')
print('-=' * 30)
