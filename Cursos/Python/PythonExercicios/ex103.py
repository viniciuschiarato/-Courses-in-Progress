#
def ficha(nome='', gols=''):
    if nome == '':
        nome = '<Desconhecido>'
    if gols == '':
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s)  no campeonato.'


input_name = str(input('Nome do jogador: ')).strip().title()
input_gols = str(input('Número de gols: '))
print(ficha(input_name, input_gols))