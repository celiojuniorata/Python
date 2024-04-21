# Desempacotamento em chamadas de métodos de funções

string = 'ABCD'
lista = ['Maria', 'João', 1, 2, 3, 'Carlos']
tupla = 'Python', 'é', 'legal'

#primeiro, b, *_, ultimo = lista
#print(primeiro, ultimo)

for nome in lista:
    print(nome, end=' ')

print('\n')

print(*lista, sep=' ')
print(*string, sep=' ')
print(*tupla, sep='||')

print('\n')
salas = [
    'ABCD',
    ['Maria', 'João', 1, 2, 3, 'Carlos'],
    'Python', 'é', 'legal'
]

print(salas)
print('\n')
print(*salas, sep='\n')