import modulos_uteis
from packageuteis import numeros

num1 = int(input('Digite um número: '))
fat1 = modulos_uteis.fatorial(num1)
print(f'O fatorial de {num1} é {fat1}.')
print(f'O dobro de {num1} é {modulos_uteis.dobro(num1)}.')
print(f'O triplo de {num1} é {modulos_uteis.triplo(num1)}.\n')

num2 = int(input('Digite um número: '))
fat2 = modulos_uteis.fatorial(num2)
print(f'O fatorial de {num2} é {fat2}.')
print(f'O dobro de {num2} é {numeros.dobro(num2)}.')
print(f'O triplo de {num2} é {numeros.triplo(num2)}.')
