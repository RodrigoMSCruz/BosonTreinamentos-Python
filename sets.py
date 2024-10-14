# Set

planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(len(planeta_anao))

print('Lua' not in planeta_anao)

for astro in planeta_anao:
    print(astro.upper(), end='')

astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
print(astros, end='')

astros_set = set(astros)
print(astros_set)

astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa Halley'}

print( astros1 != astros2)

print( astros1 | astros2)
print(astros1.union(astros2))

print(astros1 & astros2)
print(astros1.intersection(astros2))

print( astros1 ^ astros2)
print(astros1.symmetric_difference(astros2))

astros1.add('Urano')
astros1.add('Sol')
print(astros1)
#astros.remove('Plutão')
print(astros1)