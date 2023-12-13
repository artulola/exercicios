import re


def validarSenha(senha):

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!.]).{8,}$'

    if re.fullmatch(pattern, senha):
        return True
    return False

senha = 'Dedezada.25'

print(validarSenha(senha))

