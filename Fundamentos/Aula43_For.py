texto = 'Python'

i = 0
tamanho_string = len(texto)

'''
while i < tamanho_string:
    
    if texto[i] == 'o':
        break

    print(texto[i])
    i += 1
'''
texto = input('Digite uma frase: ')
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto)
