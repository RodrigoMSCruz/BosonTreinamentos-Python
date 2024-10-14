numeros = [1, 4, 7, 9, 10, 12, 21]

quadrados = list( map(lambda num: num**2, numeros) )
print(quadrados)

quadrados = [num**2 for num in numeros]
print(quadrados)

pares = [num for num in range(11) if num % 2 == 0]
print(pares)

frase = 'A lógica é apenas o princípio da sabedoria, e não seu fim'
vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í','ó', 'ú']

lista_vogais = [v for v in frase if v in vogais]
print(lista_vogais)

distributiva = [ k * m for k in [2, 3, 5] for m in [10, 20, 30]]
print(distributiva)