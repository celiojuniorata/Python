s1 = set() #Sem dados
s2 = {'Célio', 1, 3, 5} #com dados

# Sets são eficientes para remover valores duplicados de iteráveis
#   Não aceita valores mutáveis
#   Seus valores sempre serão únicos
#   Não tem índexes
#   não garantem ordem
#   são iteráveis (for, in, not in)
s2 = {1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 5}
l1 = [1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 5]

s1 = set(l1)
print('List', l1)
print('Convertei uma list em um Set',s1)

l2 = list(l1)
print('Convertei valor de um Set em list', l2)

print('Valor padrão Set', s2) #Elimina valores duplicados

l3 = set('Célio')
print('Set não garante ordem', l3)

s3 = {1, 2, 3}
#print(s3[1]) #TypeError: 'set' object is not subscriptable
print('Set não tem índices')

print('For funciona')
for numero in s3:
    print(numero + 1)

print(3 in s3) #True
print(3 not in s3) #False

# Métodos úteis:
#   add, update, clear, discard

# Operadores úteis:
# union - União - Une
# Intersecção & (intersection) - Items presentes em ambos
# Diferença - Itens presente apenas no Set da esquerda
# Diferença simétrica ^ - Itens que não estão em ambos
