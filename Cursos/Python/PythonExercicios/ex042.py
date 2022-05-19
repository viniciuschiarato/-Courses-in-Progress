#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

print('Quer saber se 3 retas conseguem fazer um triangulo?')
print('Informe o tamanho das retas')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    r = 'PODEM FORMAR'
    if r1 == r2 == r3:
        t = 'Equilátero'
    elif r1 == r2 != r3 or r2 == r3 !=r1 or r3 == r1 != r2:
        t = 'Isósceles'
    elif r1 != r2 != r3 != r1:
        t = 'Escaleno'
    print('Os segmentos a cima {} triangulo {}!'.format(r,t))
else:
    print('Os segmentos a cima NÃO FORMAM um triangulo !')



