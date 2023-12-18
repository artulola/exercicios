import re

pattern = r'<[a-z]+>'

texto = '<b>, a <html>, a <div>, a <iframe>, a <sdhhfdkjshfjkhsdfsdf>'

print(re.sub(pattern, '', texto))