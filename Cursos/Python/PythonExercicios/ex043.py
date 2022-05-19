#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
print('Calculo do IMC')
peso = float(input('informe seu peso(kg): '))
altura = (float(input('Informe sua altura(m): ')))**2
imc = peso / altura
if imc < 18.5:
    status = 'ABAIXO DO PESO'
elif imc >= 18.5 and imc <= 25:
    status = 'IDEAL'
elif imc > 25 and imc <= 30:
    status = 'SOBREPESO'
elif imc > 30 and imc <= 40:
    status = 'OBESIDADE'
elif imc > 40:
    status = 'OBESIDADE MÓBIDA'
print('O seu IMC é {:.2f} isso significa {}'.format(imc, status))

