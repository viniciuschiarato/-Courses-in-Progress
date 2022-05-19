#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
'''soma = multiplicar = maior = novosnumeros = sairdoprograma = acao = fim = 0
while fim != 1:
    numero1 = float(input('\n\nDigite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    print('\n', '-' * 10, 'MENU', '-' * 10,'\n[1] Somar''\n[2] Multiplicar''\n[3] Maior número''\n[4] Novos números''\n[5] Sair do programa')
    opcao = float(input('\nInforme a opção desejada: '))
    if opcao == 1:
        acao = numero1 + numero2
        print('A soma de {} com {} é {}.'.format(numero1, numero2, acao))
        fim = 1
    elif opcao == 2:
        acao = numero1 * numero2
        print('A multiplicação entre {} e {} resulta em {}'.format(numero1, numero2, acao))
    elif opcao == 3:
        if numero1 > numero2:
            print('O {} é maior que {}'.format(numero1, numero2))
        elif numero1 < numero2:
            print('O {} é maior que {}'.format(numero2, numero1))
        else:
            print('Não existe maior')
    elif opcao == 4:
        print('\nOk, vou reiniciar o programa.')
        fim = 2
    elif opcao == 5:
        print('\nOk, até a proxima!')
        fim = 1'''
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2 , soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando....')
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
print('Fim do programa, volte sempre!')
