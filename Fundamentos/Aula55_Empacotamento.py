#Introdução ao desempacotamento + tuples (tuplas)
#Mutáveis 

nomes = ['Célio', 'João', 'Vieira']
lista = tuple('Célio', 'João', 'Vieira') #TUple
lista2 = list(lista)
nomes = 'Célio', 'João', 'Vieira' #Tuple não pode ser alterado, adicionar etc não pode ser alterado mas funciona indice valor
nomes = ('Célio', 'João', 'Vieira') #Tuple não pode ser alterado, adicionar etc não pode ser alterado mas funciona indice valor
nome1, *resto = nomes
nome2, *_ = nomes # *_ variável não vai utilizar pega tudo
_, nome2, _ = nomes # _ variável não vai utilizar pega valor da posição
print(nome1, resto, nome2)

