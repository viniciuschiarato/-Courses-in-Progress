# print(5 + 2)  # adição
# print(5 - 2)  # subtração
# print(5 * 2)  # multiplicação
# print(5 / 2)  # divisão
# print(5 ** 2)  # potência (pow) # print(pow(5,2))
# print(5 // 2)  # divisão inteira
# print(5 % 2)  # resto da divisão
# ordem de precedência
# 1° ( )
# 2° **
# 3° *, /, // e %
# 4° + e -

# Exemplos:
#print(5 + 3 * 2)
#print(3 * 5 + 4 ** 2)
#print(3 * (5 + 4) ** 2)

# pratica
# print(pow(5,2)) # potência
# print(81**(1/2)) # raiz quadrada
# print(25**(1/2)) # raiz quadrada
# print(127**(1/3)) # raiz cubica
# print('Oi'+'Olá') # OiOlá
# print('Oi'*5) # OiOiOiOiOi
# print('='*20) # ====================
# replicando informações
# nome = input('Qual é o seu nome? ')
# print('Prazer em te conhecer {}!'.format(nome))
# print('Prazer em te conhecer {:20}!'.format(nome)) # fazer aparecer o nome num espaço de 20 caracteres
# Prazer em te conhecer vinicius            !
# print('Prazer em te conhecer {:>20}!'.format(nome)) # sinal ">" alinhamento a direita
# Prazer em te conhecer             vinicius!
# print('Prazer em te conhecer {:<20}!'.format(nome)) # sinal "<" alinhamento a esquerda
# Prazer em te conhecer vinicius            !
# print('Prazer em te conhecer {:^20}!'.format(nome)) # sinal "^" centralização
# Prazer em te conhecer       vinicius      !
# print('Prazer em te conhecer {:=^20}!'.format(nome)) # sinal "=" antes da centralização preenche os espaços vazio com este valor
# Prazer em te conhecer ======vinicius======!

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d)) # {:.3f} pede apenas 3 números depois da virgula
# print('Divisão inteira {}, e potência {}'.format(di, e))
# Um valor: 4
# Outro valor: 3
# A soma é 7, o produto é 12 e a divisão é 1.333
# Divisão inteira 1, e potência 64
# print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ') # ", end=' '" retira a quebra de linha
# print('Divisão inteira {}, e potência {}'.format(di, e))
# A soma é 16, o produto é 48 e a divisão é 3.000 Divisão inteira 3, e potência 20736
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ') # "\ n" adiciona quebra de linha
print('Divisão inteira {}, e potência {}'.format(di, e))
#desafio 5,