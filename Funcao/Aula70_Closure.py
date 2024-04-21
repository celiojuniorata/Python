'''
CLosure e funções que retornam outras funções
'''

def criar_saudacao(saudacao, nome):
    def saudar(nome):
        return  f'{saudacao}, {nome}'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia', 'Nome')
falar_boa_noite = criar_saudacao('Boa noite', 'Nome')

#print(falar_bom_dia('Luiz')) #Adiando
#print(falar_boa_noite('Luiz')) #Adiando
#print(falar_bom_dia())

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))