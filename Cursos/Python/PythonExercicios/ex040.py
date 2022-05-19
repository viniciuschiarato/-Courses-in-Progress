#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
print('Quer saber se sua média foi aprovada ou reprovada?')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    status = 'REPROVADO'
elif media >= 5 and media <= 6.9:# 6.9 > media >= 5
    status = 'RECUPERAÇÃO'
elif media >= 7:
    status = 'APROVADO'

print('Sua média é {:.2f} seu status é {}!'.format(media, status))
