import re

pattern = r'[0-9]+'

texto = 'Arthur 12231241, le4l3, 5555'

print(re.findall(pattern, texto))