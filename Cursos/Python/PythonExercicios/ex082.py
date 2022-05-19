# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
continuar = 0
geral = list()
pares = list()
impares = list()
while True:
    geral.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'S/N':
        continuar = str(input('Resposta inválida. Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
"""for n in geral:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(geral)
print(pares)
print(impares)"""
# também da certo usando o enumerate
for i, v in enumerate(geral):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(geral)
print(pares)
print(impares)