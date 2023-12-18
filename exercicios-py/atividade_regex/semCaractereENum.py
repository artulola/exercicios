import re

pattern = r'[^A-Za-z\s]'

texto = 'Arthur 2 e 3 e $*.'

print(re.sub(pattern, '', texto))