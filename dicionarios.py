# Dicionários

elemento = {
    'Z':3,
    'nome':'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(elemento['nome'])
print(elemento['densidade'])
print(f'O dicionário possui {len(elemento)} elementos.')

# Atualizar

elemento['grupo'] = 'Alcalinos'
print(elemento['grupo'])

# Adcionar uma entrada
elemento['periodo'] = 1
print(elemento['periodo'])

# Exclusão
del elemento['periodo']
print(elemento)

# Limpar todo o dicionário
# elemento.clear()

# Excluir o dicionário
# del elemento
# print(elemento)

print(elemento.items())

for i in elemento.items():
    print(i)

for i in elemento.keys():
    print(i)

for i in elemento.values():
    print(i)

for i, j in elemento.items():
    print(f'{i}: {j}')