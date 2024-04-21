#f-strings
nome = 'Ana'
altura = 1.69
peso = 65
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)