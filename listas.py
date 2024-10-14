# Lista - Representa uma sequência de valores

notas = [5, 7, 8, 6, 9]
print(notas)

n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 4]
valores = n1 + n2

print(valores)
print(valores[6])
print(valores[-1]) # Último item

valores[0] = 9
print(valores[0])
print(valores[0:2]) # A partir da posição 0, imprima 2 valores

print( len(valores) )
print( sorted(valores) )
print( sorted(valores, reverse=True ))
print(sum(valores))
print(min(valores))
print(max(valores))

valores.append(13)
print(valores)

valores.pop() #valores.pop(3)
print(valores)

valores.insert(3, 21) # Posição e valor
print(valores)

print(12 in valores)

planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print(planeta)