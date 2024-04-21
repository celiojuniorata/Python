import os 

lista = []

while True:

    print('Selecione uma opção')
    
    opcao_usuario = input('[i]nserir [a]pagar [l]istar ou [s]air: ')

    try:
        lower_opcao_usuario = opcao_usuario.lower().strip().rstrip()

        opcoes_validas = ['i', 'a', 'l', 's']

        if lower_opcao_usuario not in opcoes_validas:
            print('Opções invalida! Digite novamente...')
            continue    

        if lower_opcao_usuario == 'l' and len(lista) == 0:
            print('Nada para listar')
            continue
    except:
        print('Opção inválida! Digite novamente...')
        continue


#       APAGANDO
    if lower_opcao_usuario == 'a':
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(lista) == 0:
            print('Lista vazia, nada para apagar')
            continue

        cod_apaga = input('Escola o índice para apagar: ')

        if not cod_apaga.isdigit():
            print('índice inválido')
            continue   
        
        try:
            indice = int(cod_apaga)
            del lista[indice -1] 
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Indice não existe na lista')
        except Exception:
            print('Erro desconhecido')    
#       INSERINDO
    elif opcao_usuario == 'i':
        os.system('cls' if os.name == 'nt' else 'clear')
        valor_inserido = input('Valor: ')
        lista.append(valor_inserido)
#       CONSULTANDO     
    elif lower_opcao_usuario == 'l':
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(lista) > 0:
            print('Itens na lista:')
            for indice, valor in enumerate(lista, start=1):
                print(indice, valor)
        else:
            print('Lista vazia, nada para listar')
#       SAINDO DO SISTEMA    
    elif opcao_usuario == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Saindo do sistema.')
        break