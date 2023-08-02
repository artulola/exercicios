print("Digite sua idade com anos, meses e dias, respectivamente: ")
ano = int(input())
meses = int(input())
dias = int(input())

idade = (ano*365) + (meses * 30) + dias

print("Você possui ", idade, " dias de vida, parabéns!")