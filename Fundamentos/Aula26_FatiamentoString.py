'''

Fatiamento de strings
 012345678
 Olá Mundo
-987654321
Fatiamento [inicio:fim:passo] [::]
obs.: a funcao len retorna a qtd de caracteres'''

variavel = 'Olá Mundo'
print(variavel[4:])
print(variavel[4:8])
print(variavel[0:5])
print(variavel[-8:-2])
print(len(variavel)) # Metodo lenght
print(variavel[8:len(variavel)]) # Metodo lenght
print(variavel[0:9:2]) # Usando o passo
print(variavel[::-1]) # Usando o passo