#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print('Qual será a distância em km da sua viagem? ')
Distância = float(input('Digite aqui a kilometragem: '))
dist200 = Distância * 0.5
mdist = Distância * 0.45
if Distância <=200:
    print('O valor da passagem será: R$ {:.2f}'.format(dist200))
else:
    print('O valor da passagem será: R${:.2f}'.format(mdist))
