'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''

#Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
#print(x, y, resto) #[3, 4]

#def soma(x, y):
#    return x + y

def soma(*args):
    #args = list(args)
    #print(args, type(args))
    total = 0
    for numero in args:
        #print('total', total, numero)
        total += numero
        #print(total)
    return total

soma1 = soma(1, 2, 3, 4, 5, 6)
print(soma1)

soma2 = soma(7, 7, 13, 15, 27, -15)
print(soma2)

print(sum((7, 7, 13, 15, 27, -15)))

numero = 1, 2, 3, 4, 5, 6, 7, 8

mostra_soma = soma(*numero) #desempacotar *numero
print(mostra_soma)