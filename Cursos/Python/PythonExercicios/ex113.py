# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também
# uma função leiaFloat() com a mesma funcionalidade.

def read_int():
    while True:
        try:
            input_ = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print(f'\033[31mErro. O valor digitado não é um número inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mErro. Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return input_


def read_float():
    while True:
        try:
            input_ = str(input('Digite um número decimal: ')).replace(',', '.')
            float(input_)
        except (ValueError, TypeError):
            print(f'\033[31mErro. O valor digitado não é um número decimal.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mErro. Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return input_


print(f'O valor inteiro digitado foi {read_int()} e o real foi {read_float()}')

"""def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite  um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mErro. Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


num = leiaint('Digite um valor: ')
print(f'O valor digitado foi {num}')"""
