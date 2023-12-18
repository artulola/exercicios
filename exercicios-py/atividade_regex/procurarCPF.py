import re

pattern = r'[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}'

texto = '70660067471, 706.600.674-71, 706600674-71'

print(re.findall(pattern, texto))