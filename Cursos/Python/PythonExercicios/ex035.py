#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('Quer saber se 3 retas conseguem fazer um triangulo?')
print('Informe o tamanho das retas')

'''r1 = float(input('Digite o comprimento da reta 1 (base): '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))
if r2 - r3 < r1 < r2 + r3:
    print('Forma um triangulo')
else:
    print('Não forma um triangulo')'''
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os segmentos a cima PODEM FORMAR triangulo!')
else:print('Os segmentos a cima NÃO PODEM FORMAR um triangulo.')


