import re

def validarNumero(num):

    padrao = r'^[+-]?[0-9]+(\.[0-9]+)?$'

    if re.match(padrao, num):
        return True
    return False


print(validarNumero('-10.4'))