#Estruturas condicionais simples e composta

#if carro.esquerda(): #comando com identação colada na tela sempre sera executado
    #bloco true #comando com identação para dentro pode ou não ser executado
#else carro.direta():
    #bloco false

tempo = int(input('Quantos anos tem seu carro? '))
if tempo<=3:
    print('Carro novo')
else:
    print("Carro velho")
print("fim")