# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
"""statement = 'Loja Super Baratão'
end = 'FINALIZANDO PROGRAMA'
print('-'*60, f'\n{statement:^60}')
print('-' * 60)
name = price = continue1 = contador = soma = maisde1000 = defmaisde1000 = 0
maiorprice = menorprice = nomedomaior = nomedomenor = 0
while True:
    name = str(input('\nDigite o nome do produto: ')).strip().title()
    price = float(input('Informe o valor do produto: R$'))
    print('>Registrado.')
    if price == str:
        price = float(input('\033[31m Invalid content.\033[m\nInforme o valor do produto: R$'))
    soma += price
    contador += 1
    if price >= 1000:
        maisde1000 += 1
        if maisde1000 == 1:
            defmaisde1000 = 'produto custa'
        else:
            defmaisde1000 = 'produtos custam'
    continue1 = str(input('\nQuer inserir outro produto? [S/N]: ')).strip().upper()[0]
    if continue1 not in 'SN':
        continue1 = str(input('\033[31m Invalid content.\033[m'
                              '\nQuer inserir outro produto? [S/N]: ')).strip().upper()[0]
    if contador == 1:
        maiorprice = menorprice = price
    else:
        if price > maiorprice:
            maiorprice = price
            nomedomaior = name
        if price < menorprice:
            menorprice = price
            nomedomenor = name
    if continue1 == 'N':
        break
print('')
print('-'*20, f'{end:20}', '-'*20)
print(f'O total da compra foi R${soma:.2f}')
if maisde1000 >= 1:
    print(f'{maisde1000} {defmaisde1000} mais de mil reais')
if contador >= 2:
    print(f'O produto mais barato foi {nomedomenor} custando R${menorprice:.2f}')"""
total = totmil = menor = cont = preço = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:  # or preço < menor:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PRAGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
