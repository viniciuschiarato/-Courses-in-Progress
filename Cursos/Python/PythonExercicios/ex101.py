# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando
# se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""def voto(nasc):
    resp = 0
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        resp = 'VOTO NEGADO'
    if 65 > idade >= 18:
        resp = 'VOTO OBRIGATÓRIO'
    if 16 <= idade < 18:
        resp = 'VOTO OPCIONAL'
    if idade >= 65:
        resp = 'VOTO OPCIONAL'
    return print(f'Com {idade} anos: {resp}')


input_born = int(input('Em que ano você nasceu? '))
voto(input_born)"""


def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPICIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


input_born = int(input('Em que ano você nasceu? '))
print(voto(input_born))
