# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor dor considerado falso, a expressão inteira 
# será avalida naquele valor falso
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Tabém existe o tipo None que é usado para representar um não valor
entrada = input('[E]etrar [S]air: ')
entrada_maiuscula = entrada.upper()

senha_digitada = input('Senha: ')

senha_permitida = '123456'

#print(senha_digitada == senha_permitida)



#if entrada_maiuscula == 'E' and senha_digitada == senha_permitida:
#    print('Entrar')
#else:
#    print('Sair')

if (entrada_maiuscula == 'E' or entrada_maiuscula == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


print(0 or False or 0 or 'abc' or True) # Retorna sempre o primeiro verdadeiro

senha = input('Senha: ') or 'Sem senha'
print(senha)
