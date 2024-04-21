# Exercício com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Estorne o total para uma variável e mostre o valor da variável

def multiplica(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

valor_total = multiplica(1, 2, 3, 4, 5, 6, 7)
print(valor_total)


# Crie um função que fala se o número é par ou ímpar.
# Retorne se o número é par ou ímpar

def parImpar(numero):
    if numero % 2 == 0:
        return print(f'O número dígitado {numero} é PAR')
    return print(f'O seu número digitado {numero} é ÍMPAR')

parImpar(1778)