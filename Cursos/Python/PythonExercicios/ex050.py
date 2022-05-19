#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}° número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont = cont + 1
        if cont > 1:
            num = 'números pares'
        else:
            num = 'número par'
print('Você informou {} {} nesta sequência e a soma foi {}'.format(cont, num, soma))
