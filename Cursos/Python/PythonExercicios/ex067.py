# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado
# for negativo.
'''n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n <= 0:
        break
    contador = 0
    while contador != 10:
        contador += 1
        produto = contador * n
        print(f'{n} x {contador:2} = {produto:2}')
print('Programa tabuada encerrado. Volte sempre!')'''
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} x = {n * c}')
    print('-' * 30)
print('Programa tabuada encerrado. Volte sempre!')
