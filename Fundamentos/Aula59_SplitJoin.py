frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split(', ') #Determina aonde vai quebrar, por padrão pega por espaço
print(lista_palavras) #list

for indice in lista_palavras:
    print(indice)

frase2 = '     Olha só que, coisa de maluco      '
lista_palavras2 = frase2.split(', ')
for i, frase in enumerate(lista_palavras2):
    print(lista_palavras2[i].strip()) #Strip cortar os espaços começo e fim
    print(lista_palavras2[i].rstrip()) #Rtrip cortar os espaços direita
    print(lista_palavras2[i].lstrip()) #ltrip cortar os espaços esquerda
    lista_palavras2[i] = lista_palavras2[i].strip()

    print(lista_palavras2)

print('\n \n \n')

frase3 = '     Olha só que, coisa de maluco      '

lista_crua = []
for i, frase in enumerate(lista_palavras2):
    lista_crua.append(lista_palavras2[i].strip())

print(lista_palavras2)
print(lista_crua)


frase_unidas = '-'.join('abc')
print(frase_unidas) 