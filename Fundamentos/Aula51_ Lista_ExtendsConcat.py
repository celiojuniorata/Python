'''
Lista em Python Tipo list - Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] CRUD
'''

lista_A = [10, 20, 30, 40]
lista_B = [50, 60, 70, 80]
lista_C = lista_A + lista_B
lista_D = lista_A.extend(lista_B) #Metodo

print(lista_D) #None
print(lista_A) #10, 20, 30, 40, 50, 60, 70, 80] Mexe direto na lista A - METODO
print(lista_C) #Comportamento de extends