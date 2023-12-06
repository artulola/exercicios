import re

def extrair_numero(txt):

    padrao = r'^[()]?$'

    return re.findall(padrao, txt)

texto = 'Entre em contato atráves dos números: 1234567891 ou 987 654 321.'

print(extrair_numero(texto))