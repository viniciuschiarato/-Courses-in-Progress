#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
print('\nQuer saber qual é seu status em relação ao alistamento militar?')
print('')
print('[1] Homem\n[2] Mulher')
print('')
sexo = int(input('Selecione seu sexo: '))
if sexo == 2:
    print('Mulheres não precisam se alistar.')
else:
    print('')
    anonasc = int(input('Digite seu ano de nascimento: '))
    anoat = datetime.date.today().year
    idade = anoat - anonasc
    tempofaltante = (18 - idade)
    tempoexcedente = (idade - 18)
    anoalistamento = anoat + tempofaltante
    if idade < 18:
        print('\nStatus: IDADE INFERIOR para se alistar.')
        print('\nVocê precisa esperar mais {} ano(s) para você se aliastar. O ano do seu alistamento será {}.'.format(tempofaltante, anoalistamento))
    elif idade > 18:
        print('\nstatus: ATRASADO para se alistar.')
        print('\nVocê está a {} ano(s) em atraso com o alistamento militar'.format(tempoexcedente))
    else:
        print('\nEsta na hora de se alistar.')
