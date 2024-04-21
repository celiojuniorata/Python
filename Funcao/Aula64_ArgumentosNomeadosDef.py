'''
Argumentos nomeados e não nomeados em funções Python
Augmento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas oa rgumento (valor)
'''

def soma(x, y, z):
#Definição
    print(f'{x=} y={y} {z=}', '|', x + y + z)

print(soma) #Nome da função
print(soma(1, 2, 7)) # 3, none -> Não retorna nada
soma(2, 3, 5) 
soma(y=2, x=7, z=1) #Argumento nomeados 
soma(1, 2, z=5)

