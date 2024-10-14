# Funções built in (Internas)

valores = [2, 5, 8, -1, 0, 11, 7, -6]
print(max(valores))
print(min(valores))

a = -5
b = 4
print(abs(a))
print(pow(a, 4)) #a elevado a 4.

c = 2.789011
print(round(c, 3))

# Funções math

import math

x = 8
y = 100

raiz_quadrada = math.sqrt(x)
print(raiz_quadrada)
print(math.ceil(raiz_quadrada)) # Arredonda para o inteiro mais acima
print(math.floor(raiz_quadrada)) # Arredonda para  o inteiro mais abaixo

logaritmo = math.log10(y)
print(logaritmo)

print(math.pi)
print(math.factorial(x))

print( x / math.inf) # inf = infinito