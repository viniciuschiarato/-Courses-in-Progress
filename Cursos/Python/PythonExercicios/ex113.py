def leiaint():
    while True:
        try:
            input_ = str(input('Digite um número inteiro: '))
            while True:
                if input_.isnumeric():
                    print(f'Você digitou o número {input_}.')
                    break
                else:
                    print('\033[31mERROR. \033[mDigite um número inteiro válido.')
                    input_ = str(input('Digite um número: '))
        except Exception as erro:
            print(f'\033[31mErro {erro.__class__}. Valor digitado não é uma número inteiro. ')


leiaint()
