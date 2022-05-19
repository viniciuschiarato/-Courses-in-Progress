# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
"""bancodedados = list()
pessoa = dict()
listaidade = list()
listamulheres = list()
acimadamedia = list()
continuar = soma = media = 0
while True:
    nome =  str(input('Nome: ')).strip().title()
    pessoa['Nome'] = nome
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input('\033[31mTente outra vez.\033[m Sexo [M/F]: ')).strip().upper()[0]
    if pessoa['Sexo'] == 'F':
        listamulheres.append(nome)
    pessoa['Idade'] = int(input('Idade: '))
    listaidade.append(pessoa['Idade'])
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('\033[31mTente outra vez.\033[m Quer continuar? [S/N]: ')).strip().upper()[0]
    bancodedados.append(pessoa.copy())
    if pessoa['Idade'] >= 21:
        acimadamedia.append(pessoa.copy())
    if continuar == 'N':
        break
print('-='*30)
print(bancodedados)
print(f'- O grupo tem {len(bancodedados)} pessoas')
for v in listaidade:
    soma += v
media = soma / len(listaidade)
print(f'A média de idades é de {media:.0f} anos')
print(f'As mulheres cadastradas foram', end=' ')
print(listamulheres)
for v in listamulheres:
    print({v}, end=' ')
for v in acimadamedia:
    print()
    print(f'{v}')"""

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apemas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print(galera)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média.')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
            print()
print('<< ENCERRADO >>')
