
#def imprimir(a, b, c):
#    print(a, b, c)

#imprimir() #missing 3 required positional arguments: 'a', 'b', and 'c'
#imprimir(10, 20, 30) 
 
def imprimir(nome='Sem nome'):
    print(f'Olá {nome}')

imprimir('Célio')
imprimir('João')
imprimir() 

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é multiplo de {multiplo}?', end=' ')
    print(resultado)

multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
