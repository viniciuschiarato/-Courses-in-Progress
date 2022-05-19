# manipulando cadeias de texto
# Divisão: "split"
frase = 'Curso em Vídeo Python'
#print(frase.split()) # (gera uma lista com todas as palavras dentro da cadeia de caracteres, ou seja, cada palavra recebe indexação nova (usa os espaços como referencia))
dividido = frase.split()
print(dividido[0]) # (mostra apenas o item 0 (o primeiro)da lista)
#print(dividido[2][3]) # (mostra dentro do item 2 da lista apenas a letra 3)