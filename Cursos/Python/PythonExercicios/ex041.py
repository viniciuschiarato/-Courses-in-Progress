#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
import datetime
print('Olá atleta!')
nascimento = int(input('Informe o ano em que você nasceu: '))
anoatual = datetime.date.today().year
idade = anoatual - nascimento
if idade <= 9:
    categoria = 'MIRIM'
elif idade >= 10 and idade <= 14:
    categoria = 'INFANTIL'
elif idade >=15 and idade <=19:
    categoria = 'JUNIOR'
elif idade ==20:
    categoria = 'SÊNIOR'
elif idade > 20:
    categoria = 'MASTER'
print('Com base na sua idade {}, sua categoria é {}.'.format(idade, categoria))
