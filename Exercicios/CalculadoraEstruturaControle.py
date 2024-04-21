import time
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        limpar()

        while True:
            numero_um = input('Informe o primeiro número: ')

            if numero_um.isdigit() and numero_um != '':
                numero_um_float = float(numero_um)
            else:
                print('Digite apenas números')
                time.sleep(1)
                continue

            break

        while numero_um_float != '':
            limpar()

            operador = input('Informe o operador, que você deseja: ')

            if operador.isdigit() and operador != '':
                pass   

            operadores_validos = ['+', '-', '*', '/']

            if operador not in operadores_validos:
                print('Operador inválido')
                time.sleep(1)
                continue
            else:
                break
            
        
        while operador != '':
            limpar()

            numero_dois = input('Digite o segundo número: ')

            if numero_dois.isdigit() and numero_dois != '':
                numero_dois_float = float(numero_dois)
                pass
            else:
                print('Digite apenas números: ')
                time.sleep(1)
                continue

            break
        
        resultado = ''

        if operador == '/':
            resultado = numero_um_float / numero_dois_float
        elif operador == '*':
            resultado = numero_um_float * numero_dois_float
        elif operador == '+':
            resultado = numero_um_float + numero_dois_float
        elif operador == '-':
            resultado = numero_um_float - numero_dois_float
        else:
            print('Não deveria chegar aqui')
        
        limpar()
        print(f'O valor do seu resultado:')
        print(f'{numero_um_float} {operador} {numero_dois_float} = {resultado}')

        saida = input('Deseja sair do sistema? [S]im e [N]ão: ').lower()

        if saida == 's' and saida != '' or saida == 'sim':
            print('Saindo do sistema...')
            break
        elif saida == 'n' or saida == 'nao' or saida == 'não':
            continue
        else:
            print('Opção incorreta...')
            print('Saindo do sistema...')
            time.sleep(1)
            break


    except KeyboardInterrupt:
        print('Sistema saindo...')
        time.sleep(2)
        limpar()        
    except Exception:
        print('Erro desconhecido')


