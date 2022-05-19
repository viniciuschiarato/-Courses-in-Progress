#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Digite a velocidade: '))
multa = (velocidade - 80)
cobrança = (multa * 7)
if velocidade >80:
    print('Você foi multado!')
    print('O valor dessa multa é: R${:.2f}'.format(cobrança))
    print('Dirija com segurança!!!')
else:
    print('Tenha um bom dia! Dirija com segurança!')
