# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor dor considerado falso, a expressão inteira 
# será avalida naquele valor falso
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Tabém existe o tipo None que é usado para representar um não valor
senha = input('Senha: ')

if senha != '123456':
    print('Senha incorreta')

print(not 0)
print(not True)
print(not False)


