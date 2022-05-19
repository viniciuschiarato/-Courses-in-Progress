# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de
# trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
# de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Número da carteira de trabalho (não tem dig. 0): '))
dados['idade'] = date.today().year - nascimento
if dados['ctps'] != 0:
    dados['inicio'] = int(input('Ano da primeira contratação: '))
    dados['salário'] = float(input('Salário atual: R$'))
    dados['aposentadoria'] = dados['inicio'] + 35
    dados['aposentadoria'] = dados['aposentadoria'] - date.today().year
    dados['aposentadoria'] = dados['idade'] + dados['aposentadoria']
print('=-'*30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
