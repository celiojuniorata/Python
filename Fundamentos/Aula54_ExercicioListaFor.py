'''
Exercicio
Exiba os índices da lista

'''

lista = ['Célio', 'João', 'Vieira', 'Júnior', 1.1, 2.0, True]

indice = 0
for item in lista:
    indice += 1
    print(indice, item)


#Solução professor
lista2 = ['Célio', 'João', 'Vieira', 'Júnior', 1.1, 2.0, True]
lista2.append(11)
lista2.append(12)
lista2.append(13)

indices = range(len(lista2))
for indice in indices:
    print(indice, lista2[indice], type(lista2[indice]))