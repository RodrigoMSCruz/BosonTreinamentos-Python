# Funções - Modulurização, reuso de código, legibilidade

def soma(a, b):
    print(a + b)
    #return a + b

def subtracao(a, b):
    print(a - b)
    #return a - b

soma(12, 7)

def mult(x, y):
    return x * y

print(mult(5, 8))

def div(k, j):
    if j != 0:
        return k / j
    else:
        return 'Não é possível dividir por zero!'

if __name__ == '__main__':
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))

    r = div(a, b)
    print(f'{a} dividido por {b} é igual a {r}')

def quadrado(val):
    quadrados = []
    
    for x in val:
        quadrados.append(x ** 2)
    
    return quadrados

if __name__ == '__main__':
    valores = [2,5,7,9,12]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)

def contar(num=11, caractere='+'):
    for i in range(0, num):
        print(caractere)

if __name__ == '__main__':
    contar()
    contar(caractere='&')
    contar(num=5)
    contar(num=5, caractere='@')
