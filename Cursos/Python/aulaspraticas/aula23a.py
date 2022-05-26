try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('\033[31mInfelizmente tivemos um problema.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')
