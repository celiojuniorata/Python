'''
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
'''

print('Valor' if True else 'Outro valor')
print('Valor' if False else 'Outro valor')

print('\n')

condicao = 10 == 10
variável = 'Verdadeiro' if condicao else 'False'

print(variável)
print('\n')

digito = 2
#Valor do digito se for menor que 9 se não 0
novo_digito = digito if digito <= 9 else 0 
print(novo_digito)

novo_digito2 = 0 if digito > 9 else digito
print(novo_digito2)

print('Valor' if False else 'Outro Valor' if True else 'fim')