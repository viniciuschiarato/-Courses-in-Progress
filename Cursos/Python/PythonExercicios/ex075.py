# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
# tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
"""cont = a1 = a2 = a3 = a4 = 0
while True:
    entrada = int(input('Digite um valor: '))
    cont += 1
    if cont == 1:
        a1 = entrada
    if cont == 2:
        a2 = entrada
    if cont == 3:
        a3 = entrada
    if cont == 4:
        a4 = entrada
    if cont == 4:
        break
junto = (a1, a2, a3, a4)
print(junto)
print(f'O número 9 apareceu {junto.count(9)} nesta sequência digitada.')
print(f'O número 3 foi digitado pela primeira vez na {junto.index(3)}° posição')
#print('Os números pares são:{}'.format(junto))"""

num = ((int(input('Digite um número: '))), (int(input('Digite outro número: '))),
       (int(input('Digite mais um número: '))), (int(input('Digite o último número: '))))
print(f'Você digitou  os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu pela primeira vez na {num.index(3) + 1}° posição')
else:
    print('O valor 3 não foi encontrado.')
print(f'Os  valores pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
