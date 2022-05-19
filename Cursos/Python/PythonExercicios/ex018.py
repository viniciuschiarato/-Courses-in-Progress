#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
c = cos(radians(ang))
s = sin(radians(ang))
t = tan(radians(ang))
print('O ângulo de {:.1f} tem o SENO de {:.2f}\nO ângulo de {:.1f} tem o COSSENO de {:.2f}\n O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(ang, s, ang, c, ang, t))

'''import math
a = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O ângulo de {}tem o SENO Dde {:.2f}'.format(a, s))
print('O ângulo de {}tem o COSSENO Dde {:.2f}'.format(a, s))
print('O ângulo de {}tem o TANGENTE Dde {:.2f}'.format(a, s))'''