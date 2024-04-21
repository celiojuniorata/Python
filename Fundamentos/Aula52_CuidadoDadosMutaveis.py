'''
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
'''
lista_a = ['Célio', 'João']
#lista_b = lista_a()
lista_b = lista_a.copy() #Alterando valor da memória

lista_b[0] = 'Teste'
lista_a[1] = 'Qualquer coisa'
print(lista_b) #Mesmo valor na memória
print(lista_a) #Mesmo valor na memória