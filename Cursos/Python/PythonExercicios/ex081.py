# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numeros = list()
continuar = 0
while True:
    numeros.append(int(input('Digite um número: ')))

    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Inválido. Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram digitados {len(numeros)} números.')
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente é: {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')
