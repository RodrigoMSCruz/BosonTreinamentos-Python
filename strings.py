nome = 'Fábio'
letra = nome[2]
print(letra)
print(len(nome))

nome = 'Curso de Python'
instutor = 'Fábio'
print(nome + ' com ' + instutor)

frase = 'Vamos aprender Python hoje.'
palavras = frase.split()
print(palavras)

for palavra in palavras:
    print(palavra)

for letra in frase:
    print(letra)

print(frase[0:5])

email = input('Digite seu endereço de email: ')
arroba = email.find('@')
print(arroba)

usuario = email[0 : arroba]
dominio = email[arroba+1: ]
print(usuario)
print(dominio)

produtos = 'Carbonato de sódio e óxido de zinco'
print('sódio' in produtos)
print('magnésio' in produtos)

item = 'hipoclorito'
pos = item.find('clor')
print(pos)
pos = item.find('flu')
print(pos) # retorna -1, quer dizer que não encontrou.

objeto_celeste = 'galáxia espiral M31'
print(objeto_celeste)
print(objeto_celeste.upper())
print(objeto_celeste.lower())
print(objeto_celeste.capitalize())
print(objeto_celeste.title())

suplemento = 'cloreto de magnésio'
n_suplemento = suplemento.replace('magnésio', 'zinco')
print(suplemento)
print(n_suplemento)

frase = '    Ômega 3 é bom para saúde!   '
print(frase)
print(frase.lstrip())
print(frase.rstrip())
print(frase.strip())

fruta = 'Abacate'
print(fruta)
print(fruta.rjust(20))
print(fruta.center(20))
print(fruta.ljust(20))
print(fruta.ljust(20, "-"))
print(fruta.center(20, "-"))

p = 'Bóson Treinamentos'
print(p.startswith('Bó'))
print(p.endswith('o'))

# Docstrings
"""
Docstring é uma espécie de documentação que podemos inserir dentro
de um módulo, função ou classe no Python, entre outros locais.
Respeita deslocamento do texto e é multilinhas.
"""