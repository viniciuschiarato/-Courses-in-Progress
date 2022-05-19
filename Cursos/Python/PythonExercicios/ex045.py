#Jokenpô
import random
import time
pc = int(random.randint(1, 3))
print('\nVamos jogar Jokenpô!')
print('')
print("=" * 20)
print('>> 1 - Pedra\n>> 2 - Papel\n>> 3 - Tesoura')
print("=" * 20)
user = int(input('\nDigite seu sua jogada: '))
print('\nProcessando...')
time.sleep(2)
if pc == 1 and user == 1 or pc == 2 and user == 2 or pc == 3 and user == 3:
    resultado = 'EMPATE'
elif pc == 1 and user == 2 or pc == 2 and user == 3 or pc == 3 and user == 1:
    resultado = 'VOCÊ GANHOU'
elif pc == 1 and user == 3 or pc == 3 and user == 2 or pc == 2 and user == 1:
    resultado = 'VOCÊ PERDEU'
if pc == 1:
    rpc = 'PEDRA'
elif pc ==2:
    rpc = 'PAPEL'
elif pc == 3:
    rpc = 'TESOURA'
if user == 1:
    ruser = 'PEDRA'
elif user == 2:
    ruser = 'PAPEL'
elif user == 3:
    ruser = 'TESOURA'
print('Eu joguei {} e você jogou {}, {}!!!'.format(rpc, ruser, resultado))
