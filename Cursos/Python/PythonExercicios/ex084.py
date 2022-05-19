# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando
# tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
"""bancodedados = list()
dados = list()
nomepesomaior = list()
nomepesomenor = list()
listapeso = list()
continuar = peso = nome = 0
while True:
    nome = (str(input('Nome: ')).strip().title())
    peso = (float(input('Peso: ')))
    dados.append(nome)
    dados.append(peso)
    listapeso.append(peso)
    bancodedados.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar not in 'SN':
        continuar = str(input('Inváldo. Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
for pessoa in bancodedados:
    if pessoa[1] == max(listapeso):
        nomepesomaior.append(pessoa[0])
    if pessoa[1] == min(listapeso):
        nomepesomenor.append(pessoa[0])
print(f'Você cadastrou {len(bancodedados)} pessoas.')
print(f'O maior peso foi de {max(listapeso)}kg. Peso de {nomepesomaior}')
print(f'O menor peso foi de {min(listapeso)}kg. Peso de {nomepesomenor}')"""

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')).strip().title())
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
# print(f'Os dados foram {princ}')
print(f'O maior peso foi de {mai:.2f}kg', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {men:.2f}kg', end=' ')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
