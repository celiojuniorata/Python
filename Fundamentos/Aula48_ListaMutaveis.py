'''

Lista em Python 
Tipo list - Mutável
Supora vários valores de qualquer tipo
Conhecimento reutilizáveis - índices e fatiamento
Métodos uteis: append, insert, pop, del, clear, extend, +
'''
string = 'ABCDE' # 5 Caracteres
#print(lista, type(lista))

lista2 = []
print(bool(lista2)) #False

lista = [123, True, 'Vieira', 1.2, []]
print(lista)
lista[0] = 'Maria'
print(lista[0].upper(), type(lista[0])) #123 int
