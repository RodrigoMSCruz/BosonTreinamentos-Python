# Trocar valores entre duas variáveis

var1 = 12
var2 = 31

var2, var1 = var1, var2

# Operador Condicional Ternário
menor = var1 if var1 < var2 else var2

# Generators

valores = [1,3,5,7,9,13,15]
quadrados = (item**2 for item in valores)

# Função enumerate

bebidas = ['Café', 'Chá', 'Água', 'Suco', 'Refrigerante']
for i, item in enumerate(bebidas):
    print(f'Índice: {i}, Item: {item}')