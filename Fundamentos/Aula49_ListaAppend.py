'''
Lista em Python Tipo list - Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] CRUD
'''

lista = [10, 20 , 30, 40]
#lista[2]
#del lista[2]
#print(lista)
#print(lista[2])
lista.append(50) #Adiciona no ultima posição -  final
lista.pop() #Remove o ultimo item da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(0)
print('O item removido foi: ', ultimo_valor)
print(lista)