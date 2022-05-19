# manipulando cadeias de texto
# Análise: "len"(comprimento), "count"(contar), "find"(encontrar), "in"
frase = 'Curso em Vídeo Python'
# print(len(frase)) # (mostra o comprimento da frase, seu num de caracteres)
# print(frase.count('o')) # (contar todas as vezes que letra "o" aparece dentro da str)(o programa diferencia minúscula de maiúscula)
# print(frase.count('o',0,13)) # (contagem com fatiamento, do 0 ao 13 a quant de "o")
# print(frase.upper().count("O"))
print(frase.find('deo')) # (mostra o momento que começou a sequência str solicitada e indicando a posição no comprimento da frase)
# print(frase.find('Android')) # (se no camando "find" for colocado uma str que não existe o programa retorna -1)
# print('Curso'in frase) #(ele diz se existe ou não ,T ou F, a seq de str dentro da frase)(cuidado com letras maiúsculas)