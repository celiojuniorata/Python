# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minusculas, pode usar
# numeros e underline
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável)
# Uso: nome_variaveis = expressao

nome_completo = 'Célio Júnior'
print(nome_completo)

converta_valor = 123
print(type(str(converta_valor)), str(converta_valor), sep='-')
print(nome_completo, converta_valor, sep='/')

int_um = int('1')
print(int_um, type(str(int_um)))

nome = 'Célio'
idade = 10
maior_de_idade = idade >= 18
print('Nome: ',nome, 'Idade: ', idade, 'é maior de idade?', maior_de_idade)