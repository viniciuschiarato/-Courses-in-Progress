# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""statement = 'BANCO CEV'
end = 'FINALIZANDO PROGRAMA'
withdrawal = operation1 = quantity = counter = 0
rest = ''
notes1 = 50
notes2 = 20
notes3 = 10
notes4 = 1
print('='*50, f'\n{statement:^50}')
print('='*50)
print(f'Notas disponíveis R${notes1}, R${notes2}, R${notes3} e R${notes4}')
withdrawal = int(input('Informe a quantidade que deseja sacar: '))
while True:
    quantity = withdrawal // notes1
    rest = withdrawal % notes1
    print(f'Total de {quantity:2} cédulas de R${notes1:2},00')
    if rest > 0:
        withdrawal = rest
        notes1 = notes2
        notes2 = notes3
        notes3 = notes4
    if rest == 0:
        break
print(f'\n{end:^50}')
print('='*50, '\nVolte sempre ao banco CEV! Tenha um bom dia!')"""

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de  R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')