'''
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel:*<10}')
print(f'{variavel: ^10}') #Centro
print(f'{1000.487368548548484:.1f}')
print(f'{1000.487368548548484:,.1f}') #Colocando vírgulas
print(f'{1000.487368548548484:+,.1f}') #Colocando positivo
print(f'{-1000.487368548548484:+,.1f}') #Colocando positivo
print(f'{1000.487368548548484:0=+10,.1f}') #Colocando positivo
print(f'o Hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')