import re

pattern = r'^\[[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}\] Severidade: ?(INFO|WARNING|ERROR|DEBUG)$'

texto = '[09/02/2004 13:45:10] Severidade: ERROR'

print(re.match(pattern, texto))