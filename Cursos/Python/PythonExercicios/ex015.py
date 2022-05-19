dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
diaria = (dias*60)
kmr = (km*0.15)
total = (diaria+kmr)
print('O total a pagar é de R$ {:.2f}'.format(total))

