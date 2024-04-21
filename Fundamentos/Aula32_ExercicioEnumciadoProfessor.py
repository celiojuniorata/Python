'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informe que não é um inteiro

'''

entrada = input('Digite um número: ')

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'
    
    if par_impar is True:
        par_impar_texto = 'par'
    
    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')

'''

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação aproviada: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

'''
Dia_semana = input('Digite a hora da semana de 0 a 23: ')

Formatado_Dia_Semana = float(Dia_semana)
if Formatado_Dia_Semana >= 0 and Formatado_Dia_Semana <= 11:
    print(f'Bom dia, você digitou: {Formatado_Dia_Semana}')
elif Formatado_Dia_Semana <= 17:
    print(f'Boa tarde, você digitou: {Formatado_Dia_Semana}')
elif Formatado_Dia_Semana <= 23:
    print(f'Boa noite, você digitou: {Formatado_Dia_Semana}')
else:
    print('Valor errado ou incorreto.')
    
'''

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva: "Seu nome é curto"; se tiver entre 5 e 6 letras escreva "Seu nome é normal";
maior que 6 escreva: "Seu nome é muito grande". 

'''

Nome = input('Digite o seu nome: ')
Formatado_Tamanho_Nome = len(Nome)
print(Formatado_Tamanho_Nome)
if  Formatado_Tamanho_Nome <= 4 :
    print(f'Seu nome é muito curto:{Nome}' )
elif Formatado_Tamanho_Nome <= 6:
    print(f'Seu nome é tamanho médio: {Nome}')
else:
    print(f'Seu nome é tamanho grande: {Nome}' )