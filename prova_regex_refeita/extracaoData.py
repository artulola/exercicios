import re

pattern = r'[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}'

texto = 'Evento acontecerá no dia 1/2/2012'

print(re.search(pattern, texto))