# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for c in range(1, 501):
    if c % 3 == 0:
        s += c  # acumulador
        cont = cont + 1  # contador
print('\nA soma de todos os {} números multiplos d três de 1 até 500 é {}'.format(cont, s))
