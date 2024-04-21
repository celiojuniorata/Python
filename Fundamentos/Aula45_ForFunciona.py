'''
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador

'''

texto = 'Celio'.__iter__()
print(texto) #<str_ascii_iterator object at 0x000001E9BD3D59C0>
texto = iter('Celio')
print(texto.__next__()) #C
print(texto.__next__()) #e
print(texto.__next__()) #l
print(texto.__next__()) #i
print(next(texto)) #o
#print(texto.__next__()) #StopIteration ERRO

texto2 = 'Joao'
iterador = iter(texto2) #iterator

#for item in texto:
#    print(item)

while True:

    try:
        letra = next(iterador)
        print(letra)
        
    except StopIteration:
        print('Caiu no erro')
        break
    


