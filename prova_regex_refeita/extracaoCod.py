import re

pattern = r'PROD-[0-9]{5}-[0-9]{4}'

texto = 'codigos dos produtos: PROD-89898-4444, PROD-99999-9999, PROD-09090-0909'

print(re.findall(pattern, texto))