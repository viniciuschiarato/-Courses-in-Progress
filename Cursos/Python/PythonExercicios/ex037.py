#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número qualquer: '))
print('')
print("="*60)
print('Digite 1 para binário, 2 para octal ou 3 para hexadecimal')
print("="*60)
print('')
command = int(input('Com base na informação a cima, diga qual será a base de conversão: '))
c1 = bin(num)
c2 = oct(num)
c3 = hex(num)
if command == 1:
    print((c1)[2:]) #"[2:]"fatiamento
elif command == 2:
    print((c2)[2:])
elif command == 3:
    print((c3)[2:])
else:
    print('Opção invalida tente outra vez.')
