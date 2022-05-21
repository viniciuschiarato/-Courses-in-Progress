# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar
# de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar
# apenas um valor numérico.
# Ex: n = leiaInt('Digite um número: ')
def leiaint():
    input_ = str(input('Digite um número: '))
    while True:
        if input_.isnumeric():
            print(f'Você digitou o número {input_}.')
            break
        else:
            print('\033[31mERROR. \033[mDigite um número inteiro válido.')
            input_ = str(input('Digite um número: '))


leiaint()
