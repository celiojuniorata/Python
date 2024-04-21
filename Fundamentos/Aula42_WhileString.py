frase = 'O python é uma linguagem de programação '\
        'multiparadigma. '\
        'Python foi criado por Guido van Rossum.'

i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    apareceu_mais_vezes_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if apareceu_mais_vezes < apareceu_mais_vezes_atual:
        apareceu_mais_vezes = apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi: "{letra_apareceu_mais_vezes}" '\
      f'e sua quantidade foi de: {apareceu_mais_vezes}x')