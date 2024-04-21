import decimal #Classe interna Decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)          # 0.799999999
print(f'{numero_3:.2f}') # 0.80
print(round(numero_3, 3))
