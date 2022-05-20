from datetime import date


def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        resp = 'VOTO NEGADO'
    if 65 > idade >= 18:
        resp = 'VOTO OBRIGATÓRIO'
    if 16 < idade < 18:
        resp = 'VOTO OPCIONAL'
    if idade >= 65:
        resp = 'VOTO OPCIONAL'
    return resp


input_born = int(input('Em que ano você nasceu? '))
voto(input_born)
print(f'Com {date.today().year - input_born} anos: {voto(input_born)}')
