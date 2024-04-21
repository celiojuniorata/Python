#pip install pyspellchecker
from spellchecker import SpellChecker

def corrigindo(texto):
    spell = SpellChecker(language='pt')
    palavras = texto.split()
    texto_corrigido = []
    for palavra in palavras:
        palavra_corrigida = spell.correction(palavra)
        texto_corrigido.append(palavra_corrigida)
    return " ".join(texto_corrigido)

texto = "textp corrigido por que traz coizas sem centido"

texto_corrigido = corrigindo(texto)
print(f'Texto antigo: {texto}')
print(f'Texto novo: {texto_corrigido}')