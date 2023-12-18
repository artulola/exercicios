import re

pattern = r'\b[aeiouAEIOU][a-zA-Z]*[aeiouAEIOU]\b'

texto = 'amanda, icaro, lucas, adebayor'

print(re.findall(pattern, texto))