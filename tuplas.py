
tupla = (2, 4, 6, 7, 9)
print([tupla])

# Tuplas são imutáveis
#tupla[1] = 5

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
print(halogenios)
print(len(halogenios))
print(halogenios[3])

elementos = halogenios + gases_nobres
print(elementos)

t1 = (5,2,6,8,4,5,6,4,4,0,12,22,3,4,5)
print(t1.count(3)) #Quantas vezes o número 3 aparece?

print(halogenios[0:2])
print(halogenios[:2])
print(halogenios[-2:])
print('Cl' in halogenios)
print('Fe' in halogenios)

print(sum(t1))
print(max(t1))

#Operações não disponíveis em tuplas: .sort(, .append(), .reverse(, .pop()

for elemento in elementos:
    print(f'Elemento químico: {elemento}')

grupo17 = list(halogenios)
print(grupo17)
grupo17[0] = 'H'
print(grupo17)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tupla(grupo1)
print(alcalinos)
print(type(alcalinos))

print(sorted(alcalinos))