# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de
# cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""dados = list()
notas = list()
alunos = list()
verificacaonomes = list()
enunciado = ['N°', 'NOME', 'MÉDIA']
nome = n1 = n2 = continuar = media = contador = verificacao = continuarverificacao = 0
while True:
    nome = (str(input('Nome: ').strip().title()))
    n1 = (float(input('Nota 1: ')))
    n2 = (float(input('Nota 2: ')))
    verificacaonomes.append(nome)
    notas.append(n1)
    notas.append(n2)
    media = (n1 + n2) / 2
    dados.append(nome)
    dados.append(notas[:])
    notas.clear()
    dados.append(media)
    alunos.append(dados[:])
    dados.clear()
    alunos.sort()
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('\033[31mInválido.\033[m Quer inserir ouro aluno? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*30)
print(f'{enunciado[0]:<3}| {enunciado[1]:<12}| {enunciado[2]:<5}')
'''for c in range(0, len(alunos)):
    contador += 1'''
for conj in alunos:
    contador += 1
    print(f'{contador:<3}| ', end='')
    print(f'{conj[0]:<12}| ', end='')
    print(f'{conj[2]:<5.1f}')
while True:
    verificar = str(input('Quer fazer a verificação de notas? [S/N]: ')).strip().upper()[0]
    if verificar == 'N':
        break
    else:
        while True:
            verificacao = str(input('Mostrar notas de qual aluno? ')).strip().title()
            while verificacao not in verificacaonomes:
                verificacao = str(input('\033[31mNome inválido. \033[mMostrar notas de qual aluno? ')).strip().title()
            for v in alunos:
                if v[0] == verificacao:
                    print(f'As notas de {verificacao} são {v[1]}')

            continuarverificacao = str(input('Quer verificar notas de outro aluno? [S/N]: ')).strip().upper()[0]
            while continuarverificacao not in 'SN':
                continuarverificacao = str(input('\033[31mInválido.\033[m Quer verificar as notas de '
                                                 'outro aluno? [S/N]: ')).strip().upper()[0]
                if continuarverificacao == 'N':
                    break
            if continuarverificacao == 'N':
                break
        if continuarverificacao == 'N':
            break
"""
ficha = list()
notas = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = ((nota1 + nota2) / 2)
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar ? [S/N]: '))
    if resp in 'nN':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc ==  999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
