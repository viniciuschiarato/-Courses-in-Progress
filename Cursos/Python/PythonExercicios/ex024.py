#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
c = str(input('Digite o nome da sua cidade: ')).upper().strip()
#print(c[:5] == 'SANTO')
a = c.split()
b = ('SANTO'in a[0])
print('O nome da cidade contem a palavra "SANTO" no início? {}'.format(b))

