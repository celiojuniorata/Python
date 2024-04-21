import time
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        limpar()
        numero_um = input('Informe o primeiro número: ')
        while not numero_um.isdigit() or numero_um == '':
            print('Digite apenas números')
            time.sleep(1)
            limpar()
            numero_um = input('Informe o primeiro número: ')
        numero_um_float = float(numero_um)

        limpar()
        operador = input('Informe o operador desejado (+, -, *, /): ')
        while operador not in ['+', '-', '*', '/']:
            print('Operador inválido')
            time.sleep(1)
            limpar()
            operador = input('Informe o operador desejado (+, -, *, /): ')

        limpar()
        numero_dois = input('Informe o segundo número: ')
        while not numero_dois.isdigit() or numero_dois == '':
            print('Digite apenas números')
            time.sleep(1)
            limpar()
            numero_dois = input('Informe o segundo número: ')
        numero_dois_float = float(numero_dois)

        limpar()
        resultado = ''
        if operador == '/':
            resultado = numero_um_float / numero_dois_float
        elif operador == '*':
            resultado = numero_um_float * numero_dois_float
        elif operador == '+':
            resultado = numero_um_float + numero_dois_float
        elif operador == '-':
            resultado = numero_um_float - numero_dois_float

        print(f'O resultado é: {resultado}')

        saida = input('Deseja sair do sistema? [S]im ou [N]ão: ').lower()
        while saida not in ['s', 'sim', 'n', 'nao', 'não']:
            print('Opção incorreta...')
            saida = input('Deseja sair do sistema? [S]im ou [N]ão: ').lower()

        if saida in ['s', 'sim']:
            print('Saindo do sistema...')
            break

    except KeyboardInterrupt:
        print('Sistema saindo...')
        time.sleep(2)
        limpar()
    except Exception:
        print('Erro desconhecido')
