#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math #from math import hypot
co = float(input('Qual é o comprimento do cateto oposto? : '))
ca = float(input('Qual é o comprimento do cateto adjacente?: '))
# calc = math.sqrt((pow(co, 2))+(pow(ca, 2)))
h = math.hypot(co, ca) #"math.hypot" Calculo da hipotenusa
# print('A hipotenusa vai medir {:.2f}'.format(calc))
print('A hipotenusa vai medir {:.2f}'.format(h))
