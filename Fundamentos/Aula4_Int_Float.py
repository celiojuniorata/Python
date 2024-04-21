# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# Positivo ou negativo. int sem sinal é considerado
# Positivo
print(11) # int
print(-11) # int
print(0) # int

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante
# float sem sinal é considerado positivo
print(1.1, 10.11)
print(0.0)
print(-1.15)

# A função type mostra o tipo que o Python
# inferiu ao valor.

#print(type 1.1) SyntaxError: invalid syntax
print(type(1.1)) #<class 'float'>
print(type('Olá')) #<class 'str'>
print(type(1), type('Olá'), type(0.1)) #<class 'int'> <class 'str'> <class 'float'>