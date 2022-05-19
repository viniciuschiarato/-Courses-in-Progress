# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~
def escreva(valores):
    q = (len(valores) + 2)
    print('~' * q)
    print(f' {valores} ')
    print('~' * q)


escreva('Olá, Mundo!')
escreva('Início de funções em PYTHON')
escreva('ex097')
