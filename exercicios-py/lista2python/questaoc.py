N1 = float(input("Digite a nota do primeiro bimestre: "))
N2 = float(input("Digite a nota do segundo bimestre: "))
N3 = float(input("Digite a nota do terceiro bimestre: "))
N4 = float(input("Digite a nota do quarto bimestre: "))

MD = (N1+N2+N3+N4)/4

if (MD >= 5):
    print("Aprovado!")
else:
    print("Reprovado!")

print("Média obtida:", MD)