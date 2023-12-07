import re

def validarNumero(num):

    padrao = r'^(\(?0?[1-9]{2}[- ]?\)?)? ?([2-9]?[0-9]{4}[- ]?[0-9]{4})$'

    if re.search(padrao, num):
        return True
    return False

print(validarNumero('(84)93123457'))