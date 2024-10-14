# Funções lambda (ânonima)
# Sintaxe:
# lambda argumentos: expressão

quadrado = lambda x: x**2

for i in range (1,11):
    print(quadrado(i))


par = lambda x: x % 2 == 0

print(par(8))
print(par(9))


f_c = lambda f: (f - 32) * 5/9 # Converte celsius em fahrenheit

print(f_c(32))



# Função map()
# Sintaxe
# map(função, iterável)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dobro = list( map(lambda x: x*2, num) )
print(dobro)

palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']

maiusculas = map(str.upper, palavras)
print(list(maiusculas))

maiusculas = list( map(str.upper, palavras) )
print(maiusculas)


# Filter
# Sintaxe:
# filter(função, sequência)

def numeros_pares(n):
    return n % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
num_par = list( filter(numeros_pares, numeros) )
print(num_par)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
num_impar = list( filter( lambda x: x % 2 != 0, numeros))
print(num_impar)

# Função reduce()
# Sintaxe:
# reduce (função, sequência, valor_inicial)

from functools import reduce

def mult(x, y):
    return x * y

numeros = [1, 2, 3, 4, 5, 6] # Mesmo que 6! (Fatorial)
total = reduce(mult, numeros)
print(total)


numeros = [1, 2, 3, 4]
# (((1¹ + 2²)² + 3²)² + 4²)

total = reduce(lambda x,y: x**2 + y**2, numeros)
print(total)