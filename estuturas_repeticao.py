# While

num = 1

while(num <= 10):
    print(num)
    num += 1

nome = None

while True:
    print('Digite seu nome, ou x para parar: ')
    nome = input()
    if nome.lower() == 'x':
        break
    else:
        print(f'Bem-vindo, {nome}')
print('Até logo!')

# For

lista = [2,6,9,4,0,12,3,7]

for item in lista:
    print(item)

palavra = 'Bóson'
for letra in palavra:
    print(letra)

for numero in range(1,11):
    print(numero)

for cont_ex in range(1,6):
    print(f'\nRodada: {cont_ex}')
    for cont_in in range(5,0,-1):
        print(f'Valor: {cont_in}')
print('Fim dos laços')

import random

for A in range(1,6):
    print(f'\nConjunto {A}')
    for B in range(5):
        num = random.randint(1,100)
        print(f'Valor: {num}')