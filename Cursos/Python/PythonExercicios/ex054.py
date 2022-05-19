#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''from datetime import date
contador0 = 0
contador1 = 0
contador2 = 0
for idade in range(1, 8):
    entradaidade = int(input('Informe o ano em que a {}° pessoa nasceu: '.format(idade)))
    idadeatual = (date.today().year) - entradaidade
    contador0 += 1
    if idadeatual < 21:
        contador1 = contador1 + 1
    elif idadeatual >= 21:
        contador2 = contador2 + 1
if contador1 >= 2:
    inf1 = '{} pessoas são menores de idade'.format(contador1)
elif contador1 == 1:
    inf1 = '{} pessoa é menor de idade'.format(contador1)
elif contador1 == 0:
    inf1 = 'Não há nenhuma pessoa menor de idade informada'
if contador2 >= 2:
    inf2 = '{} pessoas são maiores de idade'.format(contador2)
elif contador2 == 1:
    inf2 = '{} pessoa é maior de idade'.format(contador2)
elif contador2 == 0:
    inf2 = 'Não há nenhuma pessoa maior de idade informada'
print('De {} idades informadas'.format(contador0))
print(inf1)
print(inf2)'''

from datetime import date
totalmaior = 0
totalmenor = 0
for pessoas in range(1, 8):
    nascimento = int(input('Informe o ano em que a {}° pessoa nasceu: '.format(pessoas)))
    idadeatual = (date.today().year) - nascimento
    if idadeatual >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalmaior))
print('E também tivemos {} pessoas menores de idade'.format(totalmenor))