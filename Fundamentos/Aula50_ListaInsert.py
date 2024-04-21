'''
Lista em Python Tipo list - Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] CRUD
'''

lista = [10, 20, 30 , 40]
lista.append('Célio')
nome = lista.pop(0)
lista.append(1233)
del lista[-1] #removendo o ultimo item da lista
print(lista, nome)

lista.insert(100, 6.0) #Indice, valor
#print(lista[100]) #list index out of range

print(lista)

#lista.clear
#print(lista)