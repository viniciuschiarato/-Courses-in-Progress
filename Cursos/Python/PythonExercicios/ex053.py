#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''frase = str(input('Digite a frase aqui: ')).strip().upper().split()
tudojunto = ''.join(frase)
inverso = ''
for letra in range(len(tudojunto) - 1, -1, -1):
    inverso = inverso + tudojunto[letra]
print('O inverso de {} é {}'.format(tudojunto, inverso))
if inverso == tudojunto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')'''

frase = str(input('Digite a frase aqui: ')).strip().upper().split()
tudojunto = ''.join(frase)
inverso = tudojunto[::-1]
print('O inverso de {} é {}'.format(tudojunto, inverso))
if inverso == tudojunto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')