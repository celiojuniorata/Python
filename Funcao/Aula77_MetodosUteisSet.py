# Métodos úteis:
#   add, update, clear, discard

s1 = {1, 2, 3}  
s1.add('Célio') #Não garante a ordem mas no caso caiu no final
s1.add(1) #Não aceita valores duplicados
s1.update('Ola´mundo') #Adiconou o Olá mundo não ordenada
s1.update((('Teste')))


print(s1)