import re

def substituir_url(txt):

    padrao = r'https?://\S+'

    return re.sub(padrao, '[LINK]', txt)

texto = 'Abra a seguinte url: http://youtube.com'

print(substituir_url(texto))