idade = 25
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
print('Pode participar do evento? ', resultado)
#print('Pode participar do evento? ' + str(resultado))

porta = 'f'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = 'Alarme disparado? ' + str(alarme)
print(msg)

tem_dinheiro = False
tem_dinheiro = not(tem_dinheiro)
msg = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg)