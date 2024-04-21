'''
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo par de "chave" e "valor"
Chaves podem ser consideradas como o "indice" que vimos na lista e podem ser
tipos imutáveis como: str, int, float, bool, tuple etc.
O valor pode ser qualquer tipo, incluindo outro dicionário
Usamos as chaves - {} - ou a classe dict para cirar dicionários
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
pessoa = {
    'nome': 'Célio Junior',
    'sobrenome': 'Vieira',
    'idade': 18,
    'altura': 1.71,
    'endereços': [
    {'rua': 'tal tal', 'numero': 123,}
    {'rua': 'outra rua', 'numero': 456},
    ]
}
'''

pessoa = {
    'nome': 'Célio Junior',
    'sobrenome': 'Vieira',
    'idade': 18,
    'altura': 1.71,
    'endereços': [
    {'rua': 'tal tal', 'numero': 123},
    {'rua': 'outra rua', 'numero': 456},
    ],
}
#pessoa = dict(nome='Carlinhos', sobrenome='Miranda')# Outra forma de usar
#print(pessoa, type(pessoa))
print(pessoa['nome']) #Acessando índice
print(pessoa['sobrenome'])
print(type (pessoa['nome']))

print('Pula linha \n')
for chave in pessoa:
    print(chave, pessoa[chave]) #Pegando os valores 

print('Pula linha \n') #Pegando apenas as chaves
for valores in pessoa:
    print(valores)