def read_int():
    try:
        input_ = int(input('Digite um número inteiro: '))
    except Exception as erro:
        print(f'\033[31mErro {erro.__class__}. O valor digitado não é um número inteiro.\033[m')
        read_int()
    else:
        return input_

def read_float():
    try:
        input_ = str(input('Digite um número decimal: ')).replace(',', '.')
        float(input_)
    except Exception as erro:
        print(f'\033[31mErro {erro.__class__}. O valor digitado não é um número inteiro.\033[m')
        read_float()
    else:
        return input_


print(f'O valor inteiro digitado foi {read_int()} e o real foi {read_float()}')
