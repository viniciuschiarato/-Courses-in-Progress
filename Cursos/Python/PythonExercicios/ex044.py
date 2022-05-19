#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

print('{:=^60}'.format(' LOJA DO VINÍCIUS '))
valororiginal = float(input('Digite o valor do(s) produto(s): R$'))
print('\nFormas de pagamento:\n>> 1 - À vista em dinheiro ou cheque: 10% de desconto.')
print('>> 2 - À vista no cartão: 5% de desconto.')
print('>> 3 - Em até 2x sem juros')
print('>> 4 - 3x ou mais no cartão: 20% de juros')
opcao = int(input('Escolha a opção de pagamento: '))
if opcao > 4 or opcao < 1:
    print('Opção invalida.')
    valorfinal = 0
elif opcao == 1:
    valorfinal = valororiginal - (valororiginal * 0.1)
elif opcao == 2:
    valorfinal = valororiginal - (valororiginal * 0.05)
elif opcao == 3:
    parcelasemjuros = valororiginal / 2
    valorfinal = valororiginal
    print('Serão geradas 2 parcelas com o valor de {:.2f}'.format(parcelasemjuros))
elif opcao == 4:
    valorfinal = valororiginal + (valororiginal * 0.2)
    print('Parcelamos este produto em até 12x')
    parcela = int(input('Informe o número de parcelas: '))
    valorparcela = valorfinal / parcela
    print('O valor das parcelas será {:.2f} COM JUROS'.format(valorparcela,))
print('O valor total do produto será R${:.2f}'.format(valorfinal))

