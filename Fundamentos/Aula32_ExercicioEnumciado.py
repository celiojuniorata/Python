'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informe que não é um inteiro

'''

while True:
    numero = input('Informe um número: ')
    
    if numero != '' and numero.isdigit():
        numero_formatado = float(numero)
        if numero_formatado % 2 == 0:
            print('Seu número é par')
        else:
            print('Seu número é ímpar')
    else:
        print('Valor incorreto')
    
    # Pergunta se o usuário deseja continuar
    continuar = input('Deseja continuar? (s/n): ')
    if continuar.lower() != 's':
        break

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