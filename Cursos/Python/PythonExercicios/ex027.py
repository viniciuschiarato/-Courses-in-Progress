#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Digite seu nome completo: ')).strip().title()
a = ((n.split()))
b = (a[0])
c = (a[len(a)-1])
print('Primeiro nome: {}'.format(b))
print('último nome: {}'.format(c))
#vinicius santos costa