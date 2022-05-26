# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios
# anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.

from package_mod.moeda_ex110 import resumo
p = int(input('Digite o preço: R$'))
resumo(p, 80, 35)
