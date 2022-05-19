pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

print(pessoas)

#print(pessoas[0])  # ERROR
print(pessoas['nome'])

print(pessoas['idade'])

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.keys())

print(pessoas.values())

print(pessoas.items())

for key in pessoas.keys():
    print(key)
print()

for key in pessoas.values():
    print(key)
print()

for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')
print()

del pessoas['sexo']
for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')
print()

pessoas['nome'] = 'Leandro'
for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')
print()

pessoas['peso'] = 98.5
for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')
print()