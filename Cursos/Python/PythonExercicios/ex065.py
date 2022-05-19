#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''from time import sleep
contador = parada = soma = continuar = maior = numero = 0
menor = 9999
while parada != 'N':
    numero = int(input('Digite um número: '))
    contador = contador + 1
    soma = numero + soma
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    continuar = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    while continuar not in 'SN':
        print('Resposta inválida. Tente novamente')
        sleep(1)
        continuar = str(input('Quer continuar? [S/N]:')).strip().upper()
    parada = continuar
média = soma / contador
print('Você digitou {} números e a média foi {}'.format(contador, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))'''

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
