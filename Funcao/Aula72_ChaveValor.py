# Manipulando chaves e valores em dicionários
pessoa = {}

pessoa['nome'] = 'Célio Júnior' #Criando chave e valor
#print(pessoa['nome1']) #Exceção KeyError
print(pessoa['nome'])

print('Pula linha \n')

chave = 'sobrenome'
pessoa[chave] = 'Maria'

print(pessoa[chave])


print('Pula linha \n')
for chaves in pessoa:
    print(chaves, pessoa[chaves])

del pessoa['sobrenome']
#print(pessoa[chave])
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])



print('Exceção para o código')