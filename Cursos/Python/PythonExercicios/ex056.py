#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
maior = 0
menor = 99999
media = 0
idadehomemmaisvelho = 0
nomehomemmaisvelho = ''
idademulhermenorde20 = 0
contadormulhermenorde20 = 0
for p in range (1, 5):
    print('-'*10, '{}° pessoa'.format(p), '-'*10)
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma = soma + idade
    media = soma / 4
    if p == 1 and sexo in 'Mm':
        idadehomemmaisvelho = idade
        nomehomemmaisvelho = nome
    if sexo in 'Mm' and idade > idadehomemmaisvelho:
        idadehomemmaisvelho = idade
        nomehomemmaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        idademulhermenorde20 = idade
        contadormulhermenorde20 += 1

print('A média de idade entre as pessoas informadas é de {:.0f} anos'.format(media))
if idadehomemmaisvelho > 0:
    print('O homen mais velho do grupo tem {} anos e se chama {}'.format(idadehomemmaisvelho, nomehomemmaisvelho))
if contadormulhermenorde20 > 0:
    print('Ao todo são {} melheres com menos de 20 anos'.format(contadormulhermenorde20))
