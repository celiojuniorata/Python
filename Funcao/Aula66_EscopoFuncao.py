'''

Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local
O escopo global é o escopo onde apenas o código é alcançavel
O escopo local é escopo onde apenas nomes do mesmo local podem ser alcançados
'''
x = 1

def escopo():
    #global x #Alterando valor x global
    x = 10

    def outra_funcao():
        #global x #Alterando valor x global
        x = 11
        y = 2
        print(x, y)

    #print(x)
    outra_funcao()

print(x)
escopo()
print(x)

#x = 1 #Erro por chamado da função antes da declaração da variável