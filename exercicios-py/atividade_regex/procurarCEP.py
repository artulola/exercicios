import re

pattern = r'\d{2}\.?\d{3}\-?\d{3}'

texto = '59.900-000, 59900000, 59900-000'

print(re.findall(pattern, texto))