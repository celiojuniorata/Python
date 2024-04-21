primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor > int_segundo_valor:
    print(f'O primeiro valor é maior {int_primeiro_valor}')
elif int_segundo_valor > int_primeiro_valor:
    print(f'O segundo valor é maior {int_segundo_valor}')
else:
    print('Valores iguais ou incorreto')