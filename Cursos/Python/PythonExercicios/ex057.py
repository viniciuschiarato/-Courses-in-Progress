#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''sexo = 0
m = 'm'
f = 'f'
while sexo != 1:
    sexo = str(input('\ndigite o seu sexo [M/F]: ')).strip().upper()[0]
    if sexo == m:
        sexo = 1
    elif sexo == f:
        sexo = 1
    else:
        print('\nResposta invalida. \n\nTente novamente.')

print('Acabou')'''
sexo = str(input('\nInforme seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\nDados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
if sexo == 'f':
    sexo = 'feminino'
else:
    sexo = 'masculino'
print('Sexo {} registrado com sucesso'.format(sexo))
