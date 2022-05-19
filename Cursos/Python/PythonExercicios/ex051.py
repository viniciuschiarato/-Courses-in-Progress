#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeirotermo = int(input('Informe o primeiro termo da P.A.: '))
razao = int(input('Informe a razão da P.A.: '))
quant = primeirotermo + (10 - 1) * razao
print('Os dez primeiros numeros são:')
for c in range(primeirotermo, quant + razao, razao):
    print('{} '.format(c), end=' ')

