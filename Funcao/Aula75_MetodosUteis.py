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

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Vieira',
}

print(p1.get('nome'))
print(p1.get('idade', 'Nome não existe'))#None valor padrão / Definir valor padrão

#nome = p1.pop('nome')
#print(nome) #Obtem o valor mas remove
#print(p1)

ultimaChave = p1.popitem() #Pega a ultima chave
print(ultimaChave)
print(p1) #{'nome': 'Luiz'}

p1.update({
    'nome': 'Novo valor'
})

print(p1) #{'nome': 'Novo valor'}

p1.update({
    'endereco': 'Rua sem saída'
})

print(p1) #{'nome': 'Novo valor', 'endereco': 'Rua sem saída'}
p1.update(nome='Vieira', idade=30)
print(p1) #{'nome': 'Vieira', 'endereco': 'Rua sem saída', 'idade': 30}

#Também funciona com lista
tupla = ('nome', 'novo valor'), #Precisa da vírgula porque tem mais de um item
p1.update(tupla)


print(p1) #{'nome': 'novo valor', 'endereco': 'Rua sem saída', 'idade': 30}