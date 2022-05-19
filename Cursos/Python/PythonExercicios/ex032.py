#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
print('Quer saber se o ano que você esta é um ano bissexto? Coloque zero para analisar o ano atual')
Ano = int(input('Digite aqui o ano: '))
if Ano == 0:
    Ano = date.today().year
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0: # "!=" diferente
    print('Sim, o ano {} é bissexto.'.format(Ano))
else:
    print('Não, o ano {} não é bissexto.'.format(Ano))