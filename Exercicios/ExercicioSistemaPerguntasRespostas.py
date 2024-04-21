# Exercicio - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é  10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


def respota(entrada, indiceResposta):
    entrada_str = str(entrada)
    if entrada_str == perguntas[indiceResposta]['Resposta']:
        return 'Respota correta'
    else:
        return 'Resposta incorreta'


def listaOpcoes(indicePergunta):
    indice = 0
    for valor in perguntas[indicePergunta]['Opções']:
        print(f'Opções: \n'
              f'{indice}) {valor}')
        indice += 1
    entrada = int(input('Escolha uma opção: '))
    return entrada

print(perguntas[0]['Pergunta'])
indice_primeira_pergunta = listaOpcoes(0) #Valor de entrada do usuário
valor_primeira_pergunta = perguntas[0]['Opções'][indice_primeira_pergunta] #Valor da opção
print(respota(valor_primeira_pergunta, 0))
print('\n')


print(perguntas[1]['Pergunta'])
indice_segunda_pergunta = listaOpcoes(1)
valor_segunda_pergunta = perguntas[1]['Opções'][indice_segunda_pergunta]
print(respota(valor_segunda_pergunta, 1))
print('\n')

print(perguntas[2]['Pergunta'])
indice_terceira_pergunta = listaOpcoes(2)
valor_segunda_pergunta = perguntas[2]['Opções'][indice_terceira_pergunta]
print(respota(valor_segunda_pergunta, 2))
print('\n')











