'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificado (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
'''
pessoa = {
    'nome': 'Célio Júnior',
    'sobrenome': 'Vieira',
}

print(pessoa.__len__()) #Nome dunder len
print(len(pessoa))
print(list(pessoa.keys())) #chaves
print(tuple(pessoa.keys())) #chaves

for chave in pessoa.keys():
    print(chave)

print(list(pessoa.values())) #Valores
print(tuple(pessoa.values())) #Valores

print(list(pessoa.items())) #Chave e valores
print(tuple(pessoa.items())) #Chave e valores

for chave, valor in pessoa.items():
    print(chave, valor)

#print(pessoa['idade']) #KeyError: 'idade'
pessoa.setdefault('idade', 0) #Uma saída
print(pessoa['idade']) #0
#print(pessoa.get('idade')) #None outra saída
print(pessoa['idade']) #0