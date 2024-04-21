'''
Retorno de valores das funções (return)
'''

#variavel = print('luiz')
variavel = None
print(variavel is None)

variavel = print('luiz')
print(variavel is None)

def soma(x, y):
    ...

variavel = soma(1, 2)
variavel = int('1')
print(variavel)


def somar(x, y):
    if x > 10:
        return [10, 20] 
    return x + y

soma1 = somar(2, 2)
soma2 = somar(12, 2)
#print(soma1 + soma2)
print(somar(11, 55))
