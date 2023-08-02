eleitores = int(input("Digite o número de eleitores da cidade: "))
validos = int(input("Quantos votos foram validos? "))
brancos = int(input("Quantos votos foram brancos? "))
nulos = int(input("Quantos votos foram nulos? "))

val100 = (validos/eleitores) * 100
bran100 = (brancos/eleitores) * 100
nul100 = (nulos/eleitores) * 100

print("Porcentagem de votos válidos:", val100,"%\nPorcentagem de votos brancos: ",bran100,"%\nPorcentagem de votos nulos: ", nul100,"%")