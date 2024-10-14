import os

os.dir('/home/rodrigomscruz/Teste')
print(f'Diretório atual: {os.getcwd()}')

padrao_nome = input('Qual padrão de nomes de arquivo a usar(Sem extensão)? ')

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, extern_arq = os.path.splittext(arq)
        nome_arq = padrao_nome + ' ' + str(contador)

        nome_novo = f'{nome_arq}{extern_arq}'
        os.rename(arq, nome_novo)

print(f'\nArquivos renomeados.')