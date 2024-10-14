# Manipulação de arquivos de texto.

'''
manipulador = open('arquivo.txt', 'r', encoding='utf-8')

print(f'\nMétodo read():\n)')
print(manipulador.read())

print(f'\nMétodo readline():\n)')
print(manipulador.readline())
print(manipulador.readline())

print(f'\nMétodo readlines():\n)')
print(manipulador.readlines())
'''

texto = input('Qual termo deseja procurar no arquivo?')

try:
    manipulador = open('arquivo.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()
        if texto in linha:
            print(f'A string foi encontrada!')
            print(linha)
        else:
            print(f'A string não foi encontrada')
        print(linha)
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()


# Escrever em arquivos de texto

try:
    manipulador = open('arquivo.txt', 'w', encoding='utf-8')
    manipulador.write('Bóson Treinamentos\n')
    manipulador.write('Como criar um arquivo de texto com Python.')    
except:
    print(f'Não foi possível abrir o arquivo.')
else:
    manipulador.close()

# Com "A", ele dá append no arquivo, sem destruir o conteúdo anterior como o bloco anterior faz.
# Ou seja, ele acrescenta no final do arquivo

try:
    manipulador = open('arquivo.txt', 'a', encoding='utf-8')
    manipulador.write('\nPython é muito empregado em IA.\n')
    manipulador.write('Inteligência Artificial veio para ficar!')    
except:
    print(f'Não foi possível abrir o arquivo.')
else:
    manipulador.close()