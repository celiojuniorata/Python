lista = ['Célio', 'João', 'Vieira']
lista.append('teste')

lista_enumerada = enumerate(lista)
print(lista_enumerada)
print(next(lista_enumerada))

enumerada = ['Teste', 1, 2, 3.30]

for item in enumerate(enumerada, start=10):
    indice, nome = item
    print(indice, nome)

#print(next(lista_enumerada)) Já consumiu tudo