#
dict_ = dict()
list_ = list()


def notas(* n, situacao=False):
    """
    => Função para analisar notas e sitações de vários alunos.
    :param n: Uma ou mais notas de alunos.
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    for v in n:
        list_.append(v)
    dict_['total'] = len(list_)
    dict_['maior'] = max(list_)
    dict_['menor'] = min(list_)
    dict_['média'] = sum(list_) / len(list_)
    if situacao:
        if sum(list_) / len(list_) >= 7:
            dict_['situação'] = 'BOA'
        if 5 >= sum(list_) / len(list_) < 7:
            dict_['situação'] = 'RAZOÁVEL'
        if sum(list_) / len(list_) < 5:
            dict_['situação'] = 'RUIM'
    return f'{dict_}'


print(notas(5.5, 9.5, 10, 6.5, situacao=True))
