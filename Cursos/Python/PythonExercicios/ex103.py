# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba
# dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa
# deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
# informado corretamente.

def ficha(nome='', gols=''):
    if nome == '':
        nome = '<Desconhecido>'
    if gols == '' or not gols.isnumeric():
        gols = 0

    return f'O jogador {nome} fez {gols} gol(s)  no campeonato.'


input_name = str(input('Nome do jogador: ')).strip().title()
input_gols = str(input('Número de gols: '))
print(ficha(input_name, input_gols))
