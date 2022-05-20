def leiaint(n):
    if n.isnumeric():
        print(f'Você digitou o numero {n}.')
    else:
        print('\033[31mERROR. Digite um número inteiro válido')


input_ = str(input('Digite um número: '))
leiaint(input_)
