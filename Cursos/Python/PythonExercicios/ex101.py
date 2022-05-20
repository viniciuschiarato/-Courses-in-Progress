#
def voto(nasc):
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
voto(input_born)
