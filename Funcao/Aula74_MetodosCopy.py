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
import copy

dicionarioUm = {
    'Nome': 'Célio Júnior',
    'Sobrenome': 'Vieira',
    'Idade': [0, 1, 2, 3],
}

dicionarioTres = dicionarioUm #Obeto original é afetado
dicionarioTres['Nome'] = 'Joãozinho'
print(dicionarioTres)

dicionarioDois = copy.deepcopy(dicionarioUm) #Jeito certo de copiar deepCopy 
dicionarioDois['Nome'] = 'Mariazinha'
print(dicionarioDois)

print(dicionarioUm)