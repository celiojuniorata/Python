palavra = 'pokemon'
armazena_letra = ''
contador = 0

while True:
    letra_usuario = input('Digite uma letra: ').strip().rstrip()
    contador += 1

    if len(letra_usuario) != 1 and letra_usuario.isalpha():
        print('Valor inválido! Digite apenas uma letra por vez')
        continue

    if len(letra_usuario) == 1:
        letra_minusculo = letra_usuario.lower()
    
    if letra_minusculo in palavra:
        armazena_letra += letra_minusculo

    resultado_palavra = ''
    for letras in palavra:
        if letras in armazena_letra:
            resultado_palavra += letras
        else:
            resultado_palavra += '*'
    
    print('Palavra formada:', resultado_palavra)

    if resultado_palavra != palavra:
        continue

    if resultado_palavra == palavra:
        print(f'Parabéns, tu acertou a palavra secreta: {resultado_palavra}')
        print(f'Você teve que tentar {contador}x vezes para acertar.')
        resultado_palavra = 0
        armazena_letra = 0
        contador = 0

    print('Agora você pode decidir se quer voltar novamente ou sair..')

    try:
        retorna = input('Aperte qualquer tecla para sair, ou (v)oltar ').lower()

        if retorna != 'v':
            break
        else:
            continue
    except:
        print('Você saiu do sistema...')
        break

    




        
