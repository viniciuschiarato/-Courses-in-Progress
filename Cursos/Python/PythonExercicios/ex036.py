#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('\nSimulação de Emprestimo Bancário')
housevalue = float(input('\nInforme o valor do imóvel: R$'))
wage = float(input('\nInforme seu salário: R$'))
numinstallments = (int(input('\nInforme em quantos anos pretende pagar: '))) * 12
vlinstallment = housevalue / numinstallments
if vlinstallment > (wage * 0.3):
    print('\nInfelizmente você não pode financiar este imovél no momento. \n\nMotivo: Mais de 30% da sua renda ficará comprometida.')
elif vlinstallment <= (wage * 0.3):
    print('\nAs condições informadas foram aceitas.\nVocê pode ser aprovado!')
