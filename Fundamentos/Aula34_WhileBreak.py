'''
Reptições
while
Executa uma ação enquanto uma condição for verdadeira
'''

condicao = True;

while condicao:
    nome = input('Qual é seu name: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')