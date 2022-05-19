#Exp 1

#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {}'.format(num,raiz))
#print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # "math.ceil()"para arredondar a o resultado da raiz para cima
#print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) # "math.floor()"para arredondar a o resultado da raiz para baixo

#Exp 2

from math import sqrt, floor # Depois de "from math import" use ctrl+sapce par aabrir a lista de funções da biblioteca selecionada.
num = int(input('Digite um número: '))
raiz = sqrt(num)
#print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))