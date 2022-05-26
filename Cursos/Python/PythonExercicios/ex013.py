v = float(input('Qual é o salário do funcionário? R$'))
a = (v+(v * 0.15))  # (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2F}, com 15% de aumento, passa a receber R${:.2F}'.format(v,a))

