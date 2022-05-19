# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nc = str(input('Digite seu nome completo: ')).strip()
u = nc.upper()
print('O nome com todas as letras maiúsculas: {}'.format(u))
lw = nc.lower()
print('O nome com todas as letras minúsculas: {}'.format(lw))
print('Seu nome tem ao todo {} letras'.format(len(nc) - nc.count(' ')))
sp = nc.split()
sp1 = len(sp[0])
print('O primeiro nome tem {} letras'.format(sp1))
#Vinicius SANTOS

