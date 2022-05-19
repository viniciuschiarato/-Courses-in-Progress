#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''primeirotermo = int(input('Informe o primeiro termo da P.A.: '))
razao = int(input('Informe a razão da P.A.: '))
termo = primeirotermo
cont = 1
mais = 1
total = 10
while mais != 0:
    while cont <= total:
        print('{} - '.format(termo),end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostra a mais? '))
    total = total + mais
print('Progressão finalizada com o total de {} termos'.format(total))'''

primeirotermo = int(input('Informe o primeiro termo da P.A.: '))
razao = int(input('Informe a razão da P.A.: '))
print('\nEstes são os primeiro 10 termos da progressão:')
contador = 0
mais = 1
total = 10
while mais != 0:
    while contador != total:
        primeirotermo = primeirotermo + razao
        print('{} '.format(primeirotermo), end='')
        contador = contador + 1
    print('Pausa')
    print('\nCaso queira encerrar o programa digite 0 na nova quantidade de termos.')
    mais = int(input('\nQuer ver mais alguns termos? Informe quantos: '))
    total = total + mais
print('Progressão encerrada. Foram mostrados um total de {} termos'.format(total))
