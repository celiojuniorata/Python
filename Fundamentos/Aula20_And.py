# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor dor considerado falso, a expressão inteira 
# será avalida naquele valor falso
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Tabé, existe o tipo None que é usado para representar um não valor
entrada = input('[E]etrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

print(senha_digitada == senha_permitida)

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(True and True and True)
print(True and 0)