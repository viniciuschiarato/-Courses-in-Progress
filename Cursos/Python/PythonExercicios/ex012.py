v = float(input('Qual é o valor do produto? R$'))
d = (v-(v * 0.05))
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(v,d))
