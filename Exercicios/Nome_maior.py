nomes = []
contador = 1

while True:
    valor_usuario = input(f'Digite o {contador}° nome (ou "0" para parar): ')
    if valor_usuario == '0':
        break
    
    if valor_usuario != '':
        nomes.append(valor_usuario)
        contador += 1
    else:
        print('Entrada inválida. Por favor, digite apenas texto.')
        continue

while True:
    ordenar_por = input('Deseja ordenar por [N]ome ou por [T]amanho do nome? ').lower()

    if ordenar_por == 'n':
        nomes_ordenados = sorted(nomes)
        print('Nomes ordenados por nome:')
        for nome in nomes_ordenados:
            print(nome)
    elif ordenar_por == 't':
        nomes_ordenados = sorted(nomes, key=len)
        print('Nomes ordenados por tamanho do nome:')
        for nome in nomes_ordenados:
            print(nome)
    else:
        print('Opção inválida.')
        continue

    print('Saindo do sistema')
    break
