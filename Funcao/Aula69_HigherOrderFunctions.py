'''
Higher Order Functions
Funções de primeira classe
'''


#saudacao2 = saudacao
#print(saudacao2('Olá'))

#v = saudacao('Bom dia')
#print(v)

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

s1 = executa(saudacao, 'Bom dia', 'Célio')
s2 = executa(saudacao, 'Bom noite', 'Maria')

print(s1)
print(s2)

