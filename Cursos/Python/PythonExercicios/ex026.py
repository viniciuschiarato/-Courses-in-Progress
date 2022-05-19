#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite sua frase: ')).strip().upper()
a = frase.count('A')
b = (frase.find('A')+1)
c = (frase.rfind('A')+1)
print('A letra "A" apareceu {} vezes'.format(a))
print('A letra "A" apareceu pela primeira vez na {}° posição'.format(b))
print('a letra "A" apareceu pela ultima vez na {}° posição'.format(c))