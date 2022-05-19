# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""aluno = dict()
n = str(input('Nome: ')).strip().title()
aluno['Nome'] = n
m = float(input(f'Média de {n}: '))
aluno['Média'] = m
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
print(aluno)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')"""

aluno = dict()
aluno['Nome'] = str(input('Nome: ')).strip().title()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print(aluno)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
