'''
Exercicio
Peça ao usuário para digitar seu nome
Peça para o usuário digitar a sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome_invertido}
        Se o nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba "Desculpe, você deixou campos vazios'''

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if (idade != '' and nome != ''):
    print(f'Seu nome é: {nome}.')
    print(f'Seu nome invertido é: {nome[::-1]}.')

    if ' ' in nome:
       print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços') 

    print(f'O seu nome tem {len(nome)} quantidade de letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A primeira letra do seu nome é {nome[len(nome) - 1]}')
else:
    print("Desculpe, você deixou campos vazios")