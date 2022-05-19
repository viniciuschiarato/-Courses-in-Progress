#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
i = float(input('Digite o salário do funcionário: R$'))
if i <= 1250:
    a = (i * 0.15)
    b = (i + a)
else:
    a = (i * 0.1)
    b = (i + a)
print('O sálario do funcionário com o aumento é: R${:.2f}'.format(b))
