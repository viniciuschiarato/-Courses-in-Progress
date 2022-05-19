#Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.
#\033[0;33;44m] #tres valores dentro do colchete 1°style; 2° text; 3°back (Não importa a ordem e o maximo de informação são 3, pode ser apenas 2 ou até mesmo 1)
#Códigos para estilo que funcionam bem: 0(none), 1(bold), 4(underline), 7(negative).
#Códigos de texto (originais, sem biblioteca): 30(branco), 31(red), 32(green), 33(yellow), 34(blue), 35(magenta), 36(cian), 37(gray)
#Códigos de back ground (originais, sem biblioteca): 40(branco), 41(red), 42(green), 43(yellow), 44(blue), 45(magenta), 46(cian), 47(gray)

#testes

print('\033[0;30;41mOlá mundo!')
print('\033[4;33;44mOlá mundo!')
print('\033[1;35;43mOlá mundo!\033[m')
print('\033[30;42mOlá mundo!')
print('\033[mOlá mundo!')
print('\033[7;30mOlá mundo!')

print('Olá mundo!')
#colorrise