'''
Interpolação básica de String
s - String
d e i - int
f - float
x e X - Hexadecimal
'''

nome = 'Célio'
preco = 1000.0000656
variavel = '%s, o preço total foi de R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (1500, 1500))