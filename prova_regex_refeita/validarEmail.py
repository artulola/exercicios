import re

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._-]+@{1}[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,}){2,}$'

    if re.match(padrao, email):
        return True
    return False

print(validar_email('arthur.lola@escolar.ifrn.edu.br'))