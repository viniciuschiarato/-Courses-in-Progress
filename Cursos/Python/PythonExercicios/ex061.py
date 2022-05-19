#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo
# e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
primeirotermo = int(input('Informe o primeiro termo da P.A.: '))
razao = int(input('Informe a razão da P.A.: '))
termo = primeirotermo
cont = 1
while cont <= 10:
    print('{} - '.format(termo),end='')
    termo += razao
    cont += 1
print('FIM')
