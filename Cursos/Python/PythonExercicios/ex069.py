# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
"""enunciado = 'CADASTRE UMA PESSOA'
fim = 'PROGRAMA FINALIZADO'
idade = sexo = continuar = quanthomem = quantmulher = quantpessoas = info1 = info2 = 0
while True:
    print('-'*50, f'\n{enunciado:^50}\n', '-'*48)
    idade = int(input('Idade: '))
    if idade < 0:
        idade = int(input('\033[31mInvalid information. Try again.\033[m\nIdade: '))
    elif idade > 120:
        idade = int(input('\033[31mInvalid information. Try again.\033[m\nIdade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo not in 'MF':
        sexo = str(input('\033[31mInvalid information. Try again.\033[m\nSexo [M/F]: ')).strip().upper()[0]
    print('-' * 50)
    continuar = str(input('Quer cadastrar outra pessoa? [S/N]: ')).strip().upper()[0]
    if idade > 18:
        quantpessoas += 1
    if sexo == 'M':
        quanthomem += 1
        if quanthomem == 1:
            info1 = 'homem'
        else:
            info1 = 'homens'
    if sexo == 'F' and idade < 20:
        quantmulher += 1
        if quantmulher == 1:
            info2 = 'mulher'
        else:
            info2 = 'mulheres'
    if continuar not in 'SN':
        continuar = str(input('\033[31mInvalid information. Try again.\033[m'
                              '\nQuer cadastrar outra pessoa? [S/N]: \n')).strip().upper()[0]
    if continuar == 'N':
        break
print('')
print('='*20, f'{fim:^9}', '='*20)
print(f'Total de pessoas com mais de 18 anos: {quantpessoas}')
if quanthomem != 0:
    print(f'Ao todo temos {quanthomem} {info1}.')
if quantmulher != 0:
    print(f'E temos {quantmulher} {info2} com menos de 20 anos.')"""
tot18 = totH = totM = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoa com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados;')
print(f'E temos {totM} mulheres com menos de 20 anos.')